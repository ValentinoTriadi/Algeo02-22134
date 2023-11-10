import urllib.request as u
import requests
from bs4 import BeautifulSoup
from PIL import Image
import time
from CBIR import colorSimiliarity
import os, shutil

start = time.time()
url = "https://valentinotriadi.github.io/"
htmldata = u.urlopen(url)
soup = BeautifulSoup(htmldata, 'html.parser') 
images = soup.find_all('img') 
# if os.path.isdir("static/dataset"):
#     shutil.rmtree("static/dataset")
# if os.path.isfile("cache.txt"):
#     os.remove("cache.txt")
count = 0
for i in images:
    full_url = ""
    # print(i['data-src'])
    # source = i['data-src']
    count += 1
    source = i.attrs['src']
    # print(source)
    if ("https://" in source or "http://" in source):
        full_url = source
    else:
        full_url = url + source
    
    data = requests.get(full_url).content 
    f = open(f'Backend/static/scrape/{count}.jpg','wb') 
    f.write(data) 
    f.close() 
    
# for i in range(count):
#     img = Image.open(f"Backend/static/dataset/{i+1}.jpg")
#     colorSimiliarity(img, True, f"{i+1}.jpg")

end = time.time()
print("Scraped",count,"images in",end-start,"s")