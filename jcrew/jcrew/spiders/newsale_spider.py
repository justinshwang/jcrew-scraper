import scrapy
import re

class NewSale(scrapy.Spider):
    # Determine if sale page has changed by looking at first 5 items
    name = "newsale"
    
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
            item_formatted = item.css(SPAN_SELECTOR).get()
            # Chooses first price if range given
            item_formatted = item_formatted.split("–")[0]
            yield {
                'price': item_formatted
            }
            count += 1         

        # filename = 'sales.html'
        # with open('jcrew/pages/' + filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)