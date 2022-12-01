from bs4 import BeautifulSoup
import requests

def scrape(site_to_scrape):
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
                scrape(site)

# main function
if __name__ =="__main__":
   
    # website to be scrape
    site="http://example.webscraping.com//"
   
    # calling function
    scrape(site)