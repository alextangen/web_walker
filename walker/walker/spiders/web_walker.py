import scrapy
from bs4 import BeautifulSoup
import requests

def to_parse(site_to_scrape):
    urls_visited = []
    site = requests.get(site_to_scrape)

    site_text = BeautifulSoup(site.text, "html.parser")

    for div in site_text.findall("a"):
        href = div.attrs['href']
        
        if href.startswith("/"):
            site = site+href
            
            if site not in urls_visited:
                urls_visited.append(site) 
                print(site)
                # calling it self
                to_parse(site)


class WebWalkerSpider(scrapy.Spider):
    name = 'web_walker'
    start_urls = ['http://www.geeksforgeeks.org/']
    follow = True

    to_parse(start_urls)