from flask import Flask, request, session
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/web-scrape")
def scrapping():
    URL = request.args.get("url")
    classname = request.args.get("main-class")
    subclass = request.args.get("sub-class")
    product = request.args.get("product-name-class")

    if URL is None:
        return "Argument not provided"
    scrapped_data = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_=classname)
    job_elements = results.find_all("div", class_=subclass)

    for job_element in job_elements:
        title_element = job_element.find("a", class_=product)     
        scrapped_data.append({'name': title_element.text.strip()})
        
    return {"products": scrapped_data}
