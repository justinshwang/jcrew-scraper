import scrapy
import re
import json
import yaml

# Retrieve URLS
START_URLS = dict()
with open ("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
for url in config["websites"]["url"]:
    START_URLS[url] = config["websites"]["url"][url]["page"]

class NewSale(scrapy.Spider):
    # Determine if sale page has changed by looking at first 5 items
    name = "new"

    def start_requests(self):
        for url in START_URLS:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parse html

        PRICE_SELECTOR = '.is-price'
        items = response.css(PRICE_SELECTOR)

        num_items = 10
        all_items_dict = {"prices":[]}

        for item in items:
            if num_items == 0:
                break
  
            SPAN_SELECTOR = 'span ::text'
            item_formatted = item.css(SPAN_SELECTOR).get()
            # Chooses first price if range given
            item_formatted = item_formatted.split("–")[0]
            # JSON Format
            # yield {
            #     'price': item_formatted
            # }
            num_items -= 1      

            all_items_dict["prices"].append(item_formatted)

        self.check_data(self, response.url, all_items_dict)


    @staticmethod
    def check_data(self, url, all_items):
        # Check for sales data, compare for updates to page
        page_name = START_URLS[url]
        filename = page_name.lower().replace(" ", "_") + ".json"
        page_path = "jcrew/updates/"
        try:
            with open(page_path + filename) as f:
                prev_sale_data = json.load(f)

            # Compare current page html with past stored version
            num_prev_items = len(prev_sale_data['prices'])
            num_new_items = len(all_items['prices'])
            if prev_sale_data == all_items or num_new_items <= num_prev_items:
                if num_new_items <= num_prev_items:
                    # Update html with fewer items 
                    with open(page_path + filename, 'w') as json_file:
                        json.dump(all_items, json_file, ensure_ascii=False, indent=4)
                print("No Changes.")
            else:
                # Send page name to stdout and used in email notification
                print("#P" + page_name + "#P" + url)
                with open(page_path + filename, 'w') as json_file:
                    json.dump(all_items, json_file, ensure_ascii=False, indent=4)
        except:
            print("#P" + page_name + "#P" + url)
            with open(page_path + filename, 'w') as json_file:
                json.dump(all_items, json_file, ensure_ascii=False, indent=4)

        self.log('Saved file %s' % filename)