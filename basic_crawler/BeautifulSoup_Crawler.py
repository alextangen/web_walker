# This was one of the initial web crawlers identified:
# https://www.geeksforgeeks.org/python-program-to-recursively-scrape-all-the-urls-of-the-website/
# This implementation will not be used for the remainder of the project, but is included for completeness.

from bs4 import BeautifulSoup
import requests

def scrape(site_to_scrape):
    urls_visited = []
    site = requests.get(site_to_scrape)

    site_text = BeautifulSoup(site.text, "html.parser")

    for div in site_text.find_all("a"):
        href = div.attrs['href']
        
        if href.startswith("/"):
            site_to_scrape = site_to_scrape + href
            
            if site_to_scrape not in urls_visited:
                urls_visited.append(site_to_scrape) 
                print(site_to_scrape)
                # calling it self
                scrape(site_to_scrape)

# main function
if __name__ =="__main__":
   
    # website to be scrape
    site="http://example.webscraping.com//"
   
    # calling function
    scrape(site)
