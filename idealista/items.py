# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdealistaItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    off = scrapy.Field()
    m2 = scrapy.Field()
    rooms = scrapy.Field()
    garage = scrapy.Field()
    floor = scrapy.Field()
    
