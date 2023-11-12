import urllib.request as u
import requests
from bs4 import BeautifulSoup
import time
import os, shutil

def imageScraper():
    start = time.time()
    url = "https://valentinotriadi.github.io/"
    htmldata = u.urlopen(url)
    soup = BeautifulSoup(htmldata, 'html.parser') 
    images = soup.find_all('img') 
    count = 0
    for i in images:
        full_url = ""
        count += 1
        source = i.attrs['src']
        if ("https://" in source or "http://" in source):
            full_url = source
        else:
            full_url = url + source
        
        data = requests.get(full_url).content 
        f = open(f'Backend/static/scrape/{count}.jpg','wb') 
        f.write(data) 
        f.close() 
        
    end = time.time()
    print("Scraped",count,"images in",end-start,"s")
    return count