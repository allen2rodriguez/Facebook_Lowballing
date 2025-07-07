# Description: Main file that runs everything 
# Author: Allen Rodriguez
# Version: 1.0.0

# TODO: Implement a way to send the AI responses to the author of the post

from offerUpWebScraper import web_scrape
from src.textGenerator import aiResponse
from src.offerUpBot import offerUpBot

def main():
    # Scrape the OfferUp listing
    page = input("Enter the OfferUp listing link: ")
    listing = web_scrape(page)

    # Data of the page - to be passed on to LLM
    title = listing[0]
    price = listing[1]
    description = listing[2]
    sellers_name = listing[3]
    data_pulled = f"Title: {title}\nPrice: {price}\nDescription: {description}\nSellers Name: {sellers_name}"
    print(data_pulled)

    # Confirmation of the information pulled
    correct_info = input("Is the information correct? (y/n): ")
    print("\n")

    # Generate the AI responses if the information is correct
    if correct_info.lower() == 'y':
        # Pass Data onto the LLM to generate a response
        # Words to pass into: cold, douche, shark, prince, victim 
        colds_response = aiResponse(data_pulled, 'cold')
        print ("coldAI's response:\n", colds_response)
        douches_response = aiResponse(data_pulled, 'douche')
        print ("doucheAI's response:\n", douches_response)
    else:
        print("Information is incorrect. Exiting...")
    # For now only using 2 bots, but can add the rest later

    # Send the AI responses to the author of the post
    cold = offerUpBot("cold", page)
    del cold # Free up memory


if __name__ == '__main__':
    main()
