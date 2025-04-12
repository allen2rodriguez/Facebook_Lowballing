# Description: Main file that runs everything 
# Author: Allen Rodriguez
# Version: 1.0.0

# TODO: Implement LLM response generation, create 5 different functions to call for each AI

from offerUpWebScraper import web_scrape
import textGenerator

def main():
    # Scrape the Offerup listing
    page = input("Enter the Offerup listing link: ")
    listing = web_scrape(page)

    # Data of the page - to be passed on to LLM
    title = listing[0]
    price = listing[1]
    description = listing[2]
    sellers_name = listing[3]

    data_pulled = f"Title: {title}\nPrice: {price}\nDescription: {description}\nSellers Name: {sellers_name}"
    print(data_pulled)

    # Pass Data onto the LLM to generate a response
    colds_response = textGenerator.coldAI(data_pulled)
    print (colds_response,"\n")

    douches_response = textGenerator.doucheAI(data_pulled)
    print (douches_response,"\n")
    
    # For now only using 2 bots, but can add the rest later

if __name__ == '__main__':
    main()
