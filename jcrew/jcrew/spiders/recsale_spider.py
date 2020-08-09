import scrapy
import re

class RecSale(scrapy.Spider):
    # Recommend top 25 sale items of interest
    name = "recsale"
    
    def start_requests(self):
        start_urls = [ 'https://www.jcrew.com/r/sale/men' ] 
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # TODO: Update selectors with xpath, select item identifying details/price
        # TODO: Check stored data (json?) for price drops

        PRICE_SELECTOR = '.is-price'
        items = response.css(PRICE_SELECTOR)

        count = 0
        num_items = 25

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