import scrapy


class WebWalkerSpider(scrapy.Spider):
    name = 'web_walker'
    allowed_domains = ['www.geeksforgeeks.org']
    start_urls = ['http://www.geeksforgeeks.org/']

    def parse(self, response):
        pass
