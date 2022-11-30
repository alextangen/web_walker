import scrapy


class WebWalkerSpider(scrapy.Spider):
    name = 'web_walker'
    start_urls = ['http://www.geeksforgeeks.org/']
    follow = True
    # start_urls = ['https://www.chevrolet.com/performance/corvette']

    def parse(self, response):
        pass
