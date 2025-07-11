from src.python_scripting.textGenerator import aiResponse, selecting_personas

# Test to make sure that aiResponse function and consistently return a string of the message
# TBD: Will eventually need to make a way to input how many messages to generate
print("Testing AI Response Generation...")
print(aiResponse(
    "N3 Elite Heavy Bag Punching Bag, $400, Sports Outdoors - Mixed martial arts & Boxing, 'N3 elite boxing training system. Heavy bag, punching bag, combination trainer. Free online training videos to train boxing/mma techniques, connects to wifi and you can download new videos. SharkTank invention. Also does cardio workouts. Almost new, was only used for while but my kids went off to college and i dont use it. Price OBO. Very heavy but can be broken into parts to fit in a van or suv.', David"
    ))

# Testing the selecting_personas function
# Making sure every single persona has the chance to be selected 
print(selecting_personas(10)) # Total of 10 personas possible