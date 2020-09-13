import scrapy


class FilterSpider(scrapy.Spider):
    name = "Amazon Nike Shoes"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/s?k=nike+shoe',
        ]
        #single identifier for each product
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        STATUS_SELECTOR = '//a[@class="a-link-normal s-no-outline"]/@href'
        products = response.xpath(STATUS_SELECTOR).getall()
        
        for product in products:
            print(product)
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''