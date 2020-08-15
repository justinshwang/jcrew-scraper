import scrapy
import re

class FilterSale(scrapy.Spider):
    # Display items given filter or label i.e. "new to sale"

    name = "filtersale"
    
    def start_requests(self):
        start_urls = [ 'https://www.jcrew.com/r/sale/men' ] 
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        filename = 'sales.html'
        with open('jcrew/pages/' + filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # # TODO: Update selectors with xpath, select item identifying details/price

        FILTER_SELECTORS = ['.best seller', '.new to sale']
        # items = response.css(PRICE_SELECTOR)
        <div class="btn--quickshop js-quickshop" data-product="AO778" data-url="/p/mens_category/shirts/classicfitshirts/shortsleeve-stretch-secret-wash-cotton-poplin-shirt-in-gingham/AO778?sale=true&amp;isFromSale=true&amp;color_name=seashore-red">QUICK SHOP
        </div></button></div>
        <div class="c-product-tile__details js-product-tile__details">
        <span class="c-badging product-tile__details">
        <div class="badging badging__container" id="badging_AO778_WX2596">
        <span class="badging__item badging__badge-title" data-qaid="arrProductListItem0Item025ProductTileProductDetailsProductBadgeLabel">
        new to sale
        </span>
        </div>
        </span>
        <a class="product-tile__details product-tile__link" data-link="/data/v1/US/sale/products/full/AO778/c/mens_category/shirts/classicfitshirts" aria-hidden="false" data-qaid="arrProductListItem0Item025ProductTileProductDetailsLink" rel="" href="/p/mens_category/shirts/classicfitshirts/shortsleeve-stretch-secret-wash-cotton-poplin-shirt-in-gingham/AO778?sale=true&amp;isFromSale=true&amp;color_name=seashore-red">
        <h3 data-qaid="arrProductListItem0Item025ProductTileProductDetailsProductDescription" class="tile__detail tile__detail--name">Short-sleeve stretch Secret Wash cotton poplin shirt in gingham</h3><div class="tile__detail tile__detail--price">
        <div id="productPriceNormalWas-AO778WX2596" class="tile__detail tile__detail--price--was">
        
        <span class="badging__item badging__icon-badge">
        <img alt="" aria-hidden="true" src="https://www.jcrew.com/s7-img-facade/TS" data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductBadgeImage"/>
        </span>
        <span class="badging__item badging__badge-title" data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductBadgeLabel">
        best seller
        </span>
        </div>
        </span>
        <a class="product-tile__details product-tile__link" data-link="/data/v1/US/sale/products/full/J1785/c/mens_category/tshirts" aria-hidden="false" data-qaid="arrProductListItem0Item028ProductTileProductDetailsLink" rel="" href="/p/mens_category/tshirts/garmentdyed-slub-cotton-crewneck-tshirt/J1785?sale=true&amp;isFromSale=true&amp;color_name=lavender">
        <h3 data-qaid="arrProductListItem0Item028ProductTileProductDetailsProductDescription" class="tile__detail tile__detail--name">
        # count = 0
        # num_items = 25

        # for item in items:
        #     if count > num_items:
        #         break
        #     SPAN_SELECTOR = 'span ::text'
        #     item_formatted = item.css(SPAN_SELECTOR).get()
        #     # Chooses first price if range given
        #     item_formatted = item_formatted.split("–")[0]
        #     yield {
        #         'price': item_formatted
        #     }
        #     count += 1         
