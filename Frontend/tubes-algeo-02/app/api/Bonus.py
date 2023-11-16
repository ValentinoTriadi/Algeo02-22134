import urllib.request as u
import requests
from bs4 import BeautifulSoup
import time, os, json
import pdfkit
import jinja2



def imageScraper(url):
    start = time.time()
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


def render_html(jsonfile):
    """
    Render html page using jinja based on layout.html
    """
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "pdf.html"
    template = template_env.get_template(template_file)
    output_text = template.render(
        path = os.getcwd(),
        items = jsonfile,
        )

    html_path = './PDFResult.html'
    html_file = open(html_path, 'w')
    html_file.write(output_text)
    html_file.close()
    pdf_path = f'./PDFResult.pdf'    
    html2pdf(html_path, pdf_path)   

def html2pdf(html_path, pdf_path):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.35in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options)

def exportPDF():

    f = open("./hasil.json", 'r')
    lines = f.read()
    f.close()

    lines = json.loads(lines)

    render_html(lines)