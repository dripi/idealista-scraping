# -*- coding: utf-8 -*-
__author__ = 'Adrián Quijada'
import scrapy
from idealista.items import IdealistaItem
from scrapy.spiders import CrawlSpider
from datetime import datetime
import numpy as np

class IdealistacrawlerSpider(scrapy.Spider):
    name = "idealistaCrawler"
    allowed_domains = ['idealista.com']
    start_urls = []
    
    #Setting number of pages to scrap (by default 50)
    for i in np.arange(1, 50):
        start_urls.append('https://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-' + str(i) + '.htm')
    
    #Proccessing the number of pages set before through "parse"
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)
    
    #Parsing the requests in order to extract the data
    def parse(self, response):
        links = []
        titles = []
        prices = []
        offs = []
        rooms = []
        m2 = []
        floors = []
        descs = []
        garages = []
        
        for info in response.xpath("//*[@class='item-info-container']"):
            links.append(str(''.join("https://www.idealista.com" + info.xpath('a/@href').extract().pop())))
            titles.append(info.xpath('a/@title').extract().pop())
            rooms.append('' if len(info.xpath('span[@class="item-detail"]/small[contains(text(), "hab")]/../text()').extract()) < 1 else info.xpath('span[@class="item-detail"]/small[contains(text(), "hab")]/../text()').extract().pop().strip())
            m2.append('' if len(info.xpath('span[@class="item-detail"]/small[starts-with(text(), "m")]/../text()').extract()) < 1 else info.xpath('span[@class="item-detail"]/small[starts-with(text(), "m")]/../text()').extract().pop().strip())
            floors.append('' if len(info.xpath('span[@class="item-detail"][contains(text(), "Bajo") or contains(text(), "Ent") or contains(small/text(), "planta")]/text()').extract()) < 1 else info.xpath('span[@class="item-detail"][contains(text(), "Bajo") or contains(text(), "Ent") or contains(small/text(), "planta")]/text()').extract().pop().strip())
        
        for row in response.xpath("//*[@class='row price-row clearfix']"):
            prices.append(row.xpath("span[@class='item-price h2-simulated']/text()").extract().pop().replace('.', ''))
            garages.append(1 if len(row.xpath("span[@class='item-parking']/text()").extract()) > 0 else 0)
            offs.append(0 if len(row.xpath("./*[@class='item-price-down icon-pricedown']/text()").extract()) < 1 else row.xpath("./*[@class='item-price-down icon-pricedown']/text()").extract().pop().replace('.','').strip().split(' ').pop(0))
        
        results = zip(links, titles, prices, offs, m2, rooms, garages, floors)
        
        for flat in results:
            item = IdealistaItem(date = datetime.now().strftime('%d-%m-%Y'), link = flat[0], title = flat[1], price = flat[2], off = flat[3], m2 = flat[4], rooms = flat[5], garage = flat[6], floor = flat[7])
            yield item