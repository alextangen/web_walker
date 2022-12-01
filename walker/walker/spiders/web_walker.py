# The base of this code was copied from the below link:
# https://www.proxiesapi.com/blog/recursively-scraping-webpages-with-scrapy.html.php
# We will still be obeying the ROBOTS.txt file, and we will be taking in 'start_urls' 
# from the google_search.py file.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WebWalkerSpider(CrawlSpider):
    name = 'web_walker'
    # start_urls = ['http://www.geeksforgeeks.org/']
    start_urls = []
    cont = True

    # Want to read in seeds from file walker_seeds.txt
    seeds = open('walker/spiders/walker_seeds.txt', 'r')
    num_url = 0

    while cont:
        num_url += 1
        url = seeds.readline()
        print("Read URL: " + url)
        start_urls += [url]

        if not url:
            cont = False
            break

    print("Array of URLs: " + str(len(start_urls)))

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

        # In here, we should parse the page, identify the count of words that 
        # match the keywords, and weight them according to matches and extensions

        # filename = 'storage/' response.url.split("/")[-1]   '.html'
        # print('Saving as :' filename)
        # with open(filename, 'wb') as f:
        #    f.write(response.body)
