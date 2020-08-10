import scrapy
import re
import json

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

        all_items_dict = {"prices":[]}
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

            all_items_dict["prices"].append(item_formatted)

        filename = "newsales.json"
        page_path = "jcrew/pages/"
        try:
            # Sales data exists, check for changes
            with open(page_path + filename) as f:
                prev_sale_data = json.load(f)
            if prev_sale_data == all_items_dict:
                print("It's the same!!")
            else:
                print("New sales page!")
                with open(page_path + filename, 'w') as json_file:
                    json.dump(all_items_dict, json_file, ensure_ascii=False, indent=4)
        except:
            print("New sales page!")
            with open(page_path + filename, 'w') as json_file:
                json.dump(all_items_dict, json_file, ensure_ascii=False, indent=4)

        self.log('Saved file %s' % filename)