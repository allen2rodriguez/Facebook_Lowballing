# Description: Main file that runs everything 
# Author: Allen Rodriguez
# Version: 1.0.0

from flask import Flask, request, jsonify
import json

from offerUpBot import offerUpBot
from textGenerator import aiResponse, selecting_personas

page = "https://offerup.com/item/detail/90f989df-0eff-3eb3-9065-ed9749f25857"

app = Flask(__name__)

'''
Arguments should get the number of pots need and the page that the js is currently on
'''
@app.route('/')
def main():
    personas = selecting_personas(3)
    bot = offerUpBot(page)
    scraped_content = bot.web_scrape()
    data = {
    'personas': personas,
    'scraped_content': scraped_content
    }
    responses = aiResponse(json.dumps(data))
    ship2AI = jsonify(data)
    print(responses)
    return ship2AI
    


if __name__ == '__main__':
    app.run(debug=True)