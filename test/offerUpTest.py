'''
Price: info[0]
Categoriory: info[2]
Sellers_Name: info[5]
Description: info[7]
'''
from offerUpWebScraper import web_scrape

'''
Go through all the links in the .txt file and see how many elements have the p tag.
'''

''''
List out all the elements that have the p tag and write them to a file.

with open('links2test.txt', 'r') as f, open("writeFile.txt", "a") as x:
    for line in f:
        listing = web_scrape(line.strip())
        print(len(listing[1]))
        info_text = '\n'.join([element.text for element in listing[1]])
        x.write(info_text + '\n')  # Write the joined text to the file
'''

# Print out the length of the list 
f = open('links2test.txt', 'r')
for line in f:
    listing = web_scrape(line.strip())
    print(len(listing[1]))  # Print the length of the list



