# Práctica 1: Idealista scraping
## Descripción:
El spider realiza una extracción de datos del sitio web www.idealista.com, en concreto, de los inmuebles en venta de la ciudad de Barcelona y genera un dataset.

## Requerimientos
- Desde Anaconda:
``
conda install scrapy
``

- Desde pip:
``
pip install scrapy
``

## Cómo ejecutar:
Desde el directorio principal del proyecto (idealista) ejecutar:
```
scrapy crawl idealistaCrawler -o dataset.csv
```
