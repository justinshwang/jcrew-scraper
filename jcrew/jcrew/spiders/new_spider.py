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
            # Print json outputted
            # yield {
            #     'price': item_formatted
            # }
            count += 1         

            all_items_dict["prices"].append(item_formatted)

        page_name = START_URLS[url]
        self.check_data(self, page_name, all_items_dict)

    # def build_datadoc (self, row, name, price):
    #     tablerows = response.xpath("//*[@id='results']/tr")
    #     for row in tablerows:
    #     return { 'name': name,
    #             'price': row.xpath("./td[@class='was-price' or  @class='is-price']/a/text()").extract_first(),
    #             '_idx': row.xpath("./td[5]/text()").extract_first()
    #     }

    @staticmethod
    def check_data(self, page_name, all_items):
        # Check for sales data, compare for updates to page
        filename = page_name.lower().replace(" ", "_") + ".json"
        page_path = "jcrew/updates/"
        try:
            with open(page_path + filename) as f:
                prev_sale_data = json.load(f)
            if prev_sale_data == all_items:
                print("No Changes.")
            else:
                # Send page name to stdout and used in email notification
                print(page_name)
                with open(page_path + filename, 'w') as json_file:
                    json.dump(all_items, json_file, ensure_ascii=False, indent=4)
        except:
            print(page_name)
            with open(page_path + filename, 'w') as json_file:
                json.dump(all_items, json_file, ensure_ascii=False, indent=4)

        self.log('Saved file %s' % filename)

    