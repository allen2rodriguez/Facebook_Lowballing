# This page will be used to gather inforomation by webscrapping the page
import requests
from bs4 import BeautifulSoup

page = input("Enter the link: ")
page_to_scrap = requests.get(page)

# Parse the HTML    
soup = BeautifulSoup(page_to_scrap.text, 'html.parser')

title = soup.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u')
description = soup.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr40x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u')
sellers_name = soup.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x6prxxf xvq8zen x1s688f xzsf02u')
price = soup.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u')
# If a vechile, also scrape the the "About this vehicle" information 


print(title, description, sellers_name )