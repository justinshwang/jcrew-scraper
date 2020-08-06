import scrapy
import re

class JcrewSaleMens(scrapy.Spider):
    name = "jcrewsalemens"
    start_urls = [ 'https://www.jcrew.com/r/sale/men' ] 
