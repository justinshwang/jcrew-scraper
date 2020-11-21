import scrapy
import re
import json
import yaml

# Retrieve URLS
START_URLS = dict()
with open ("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
questions = config['options']['graphs']
# Defaults when running multiple graphs
iteration_num = config['options']['iterationNum']
cumulative = config['options']['graphCumulatively']
team_num = config['options']['teamNum']


class NewSale(scrapy.Spider):
    # Determine if sale page has changed by looking at first 5 items

    name = "new"
    
    def start_requests(self):
        for url in START_URLS:
            self.page_name = START_URLS[url]
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

        self.check_data(self, all_items_dict)

    # def build_datadoc (self, row, name, price):
    #     tablerows = response.xpath("//*[@id='results']/tr")
    #     for row in tablerows:
    #     return { 'name': name,
    #             'price': row.xpath("./td[@class='was-price' or  @class='is-price']/a/text()").extract_first(),
    #             '_idx': row.xpath("./td[5]/text()").extract_first()
    #     }

    @staticmethod
    def check_data(self, all_items):
        # Check for sales data, compare for updates to page
        filename = self.page_name + ".json"
        page_path = "jcrew/updates/"
        try:
            with open(page_path + filename) as f:
                prev_sale_data = json.load(f)
            if prev_sale_data == all_items:
                print("No Changes.")
            else:
                print(self.page_name)
                with open(page_path + filename, 'w') as json_file:
                    json.dump(all_items, json_file, ensure_ascii=False, indent=4)
        except:
            print("Sales page has been updated recently.")
            with open(page_path + filename, 'w') as json_file:
                json.dump(all_items, json_file, ensure_ascii=False, indent=4)

        self.log('Saved file %s' % filename)

    