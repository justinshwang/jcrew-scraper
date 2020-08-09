import scrapy
import re

class JcrewNewSale(scrapy.Spider):
    name = "jcrewnewsale"
    
    def start_requests(self):
        start_urls = [ 'https://www.jcrew.com/r/sale/men' ] 
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        PRICE_SELECTOR = '.is-price'
        items = response.css(PRICE_SELECTOR)

        count = 0
        num_items = 5


        for item in items:
            if count > num_items:
                break
            SPAN_SELECTOR = 'span ::text'
            yield {
                'price': item.css(SPAN_SELECTOR).get()
            }
            count += 1         

        # filename = 'sales.html'
        # with open('jcrew/pages/' + filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)