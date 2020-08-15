import scrapy
import sys
import re
import json

class FilterSale(scrapy.Spider):
    # Display items given filter or label i.e. "new to sale"

    name = "filter"
    
    def start_requests(self):
        start_urls = [ 'https://www.jcrew.com/r/sale/men' ] 
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        filename = 'sales.html'
        with open('jcrew/pages/' + filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # TODO: Update selectors with xpath, select item identifying details/price
        STATUS_SELECTOR = '.badging__badge-title'
        status_options = ['best seller', 'new to sale']
        all_items_dict = {"Items":[]}
        items = response.css(STATUS_SELECTOR)

        for item in items:
            SPAN_SELECTOR = 'span ::text'

            if (item.css(SPAN_SELECTOR).get() in status_options):
                # Replace "BadgeLabel" substring
                item_qaid = item.xpath('@data-qaid').get().replace("BadgeLabel", "Description")
                item_name = response.xpath('//h3[@data-qaid=$val]/text()', val=item_qaid).get() 
  
                yield {
                    'Item': item_name
                }
                all_items_dict["Items"].append(item_name)

        self.check_data(self, all_items_dict)

    @staticmethod
    def check_data(self, all_items):
        # Check for sales data, compare for updates to page

        filename = "newsales.json"
        page_path = "jcrew/updates/"
        try:
            with open(page_path + filename) as f:
                prev_sale_data = json.load(f)
            if prev_sale_data == all_items:
                print("No New Items.")
            else:
                print("New Items have been added recently.")
                with open(page_path + filename, 'w') as json_file:
                    json.dump(all_items, json_file, ensure_ascii=False, indent=4)
        except:
            print("New Items have been added recently.")
            with open(page_path + filename, 'w') as json_file:
                json.dump(all_items, json_file, ensure_ascii=False, indent=4)

        self.log('Saved file %s' % filename)

        # <div class="btn--quickshop js-quickshop" data-product="AO778" data-url="/p/mens_category/shirts/classicfitshirts/shortsleeve-stretch-secret-wash-cotton-poplin-shirt-in-gingham/AO778?sale=true&amp;isFromSale=true&amp;color_name=seashore-red">QUICK SHOP
        # </div></button></div>
        # <div class="c-product-tile__details js-product-tile__details">
        # <span class="c-badging product-tile__details">
        # <div class="badging badging__container" id="badging_AO778_WX2596">
        # <span class="badging__item badging__badge-title" data-qaid="arrProductListItem0Item025ProductTileProductDetailsProductBadgeLabel">
        # new to sale
        # </span>
        # </div>
        # </span>
        # <a class="product-tile__details product-tile__link" data-link="/data/v1/US/sale/products/full/AO778/c/mens_category/shirts/classicfitshirts" aria-hidden="false" data-qaid="arrProductListItem0Item025ProductTileProductDetailsLink" rel="" href="/p/mens_category/shirts/classicfitshirts/shortsleeve-stretch-secret-wash-cotton-poplin-shirt-in-gingham/AO778?sale=true&amp;isFromSale=true&amp;color_name=seashore-red">
        # <h3 data-qaid="arrProductListItem0Item025ProductTileProductDetailsProductDescription" class="tile__detail tile__detail--name">Short-sleeve stretch Secret Wash cotton poplin shirt in gingham</h3><div class="tile__detail tile__detail--price">
        # <div id="productPriceNormalWas-AO778WX2596" class="tile__detail tile__detail--price--was">
        
        # <span class="badging__item badging__icon-badge">
        # <img alt="" aria-hidden="true" src="https://www.jcrew.com/s7-img-facade/TS" data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductBadgeImage"/>
        # </span>
        # <span class="badging__item badging__badge-title" data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductBadgeLabel">
        # best seller
        # </span>
        # </div>
        # </span>
        # <a class="product-tile__details product-tile__link" data-link="/data/v1/US/sale/products/full/J1785/c/mens_category/tshirts" aria-hidden="false" data-qaid="arrProductListItem0Item028ProductTileProductDetailsLink" rel="" href="/p/mens_category/tshirts/garmentdyed-slub-cotton-crewneck-tshirt/J1785?sale=true&amp;isFromSale=true&amp;color_name=lavender">
        # <h3 data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductDescription" class="tile__detail tile__detail--name">

           
