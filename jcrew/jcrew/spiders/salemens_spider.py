import scrapy
import re

class JcrewSale(scrapy.Spider):
    name = "jcrewsale"
    
    def start_requests(self):
        start_urls = [ 'https://www.jcrew.com/r/sale/men/shoes_sneakers?crawl=yes' ] 
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'sales.html'
        with open('jcrew/pages/' + filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)