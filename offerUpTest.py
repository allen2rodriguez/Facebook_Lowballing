# Description: Go through all the links in the .txt file and see how many elements have the p tag.
# Test Link: https://offerup.com/item/detail/a368f8c6-2e36-33f1-b3fa-d96f3430e200

'''
Price: info[0]
Categoriory: info[2]
Sellers_Name: info[5]
Description: info[7]
'''
from offerUpWebScraper import web_scrape


# Figure out how to get the specific class name for each page (e.i. jss583) Because thats the way to get the description



# Print out the length of the list 
f = open('test/links2test.txt', 'r')
for line in f:
    listing = web_scrape(line.strip())
    print(listing[0], )



