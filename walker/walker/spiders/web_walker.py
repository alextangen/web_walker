import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WebWalkerSpider(scrapy.CrawlSpider):
    name = 'web_walker'
    start_urls = ['http://www.geeksforgeeks.org/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    custom_settings = {
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 25,
        'CONCURRENT_ITEMS': 100,
        'REACTOR_THREADPOOL_MAXSIZE': 400,
        # Hides printing item dicts
        'LOG_LEVEL': 'INFO',
        'RETRY_ENABLED': False,
        'REDIRECT_MAX_TIMES': 1,
        # Stops loading page after 5mb
        'DOWNLOAD_MAXSIZE': 5592405,
        # Grabs xpath before site finish loading
        'DOWNLOAD_FAIL_ON_DATALOSS': False,

        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE' :'scrapy.squeues.FifoMemoryQueue'
    }


    def parse_item(self, response):
        print('Downloaded... ' + response.url)
        # filename = 'storage/' response.url.split("/")[-1]   '.html'
        # print('Saving as :' filename)
        # with open(filename, 'wb') as f:
        #    f.write(response.body)