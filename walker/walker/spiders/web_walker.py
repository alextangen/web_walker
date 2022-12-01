import scrapy
from bs4 import BeautifulSoup
import requests

class WebWalkerSpider(scrapy.Spider):
    name = 'web_walker'
    start_urls = ['http://www.geeksforgeeks.org/']
    follow = True

    def parser(site_to_scrape):
        site = requests.get(site_to_scrape)

        site_text = BeautifulSoup(site.text, "html.parser")

        for div in site_text.findall("a"):


    def parse(self, response):
        pass
