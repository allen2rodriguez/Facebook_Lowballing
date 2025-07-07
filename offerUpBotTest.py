from src.offerUpBot import offerUpBot

test_bot = offerUpBot("https://offerup.com/item/detail/c85174c8-6724-3ca3-a912-8ea718dae5d4?cid=7.3")

# Test the web_scrape method
listing = test_bot.web_scrape()
print("Listing Information:")
for item in listing:
    print("\t" + item)

# Test the send_message method