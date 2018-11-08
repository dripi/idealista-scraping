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

## Componentes:
**Adrián Quijada Gomariz**

## Descripción de ficheros:
* _idealista/spiders/idealistaCrawler.py:_ contiene la lógica principal del crawler. Donde se realiza la conexión con la web, la selección de elementos a descargar y la descarga/recopilación de datos.
* _idealista/items.py:_ contiene la definición de la clase Idealista, que el crawler utiliza para incrustar los datos que serán descargados.
* _idealista/middlewares.py:_ se utiliza para crear las funcionalidades personalizadas a la hora de procesar las respuestas que recibe el crawler. En este caso el archivo se ha creado por defecto por el framework Scrapy.
* _idealista/pipelines.py:_ se utiliza para definir pipelines personalizadas. Cuando un objeto de la clase definida en items.py es procesado por el crawler se envía automáticamente a una pipeline donde recibe un tratamiento secuencial. En este caso el archivo se ha creado por defecto por el framework Scrapy.
* _idealista/settings.py:_ contiene la configuración de Scrapy y del crawler en cuestión.

