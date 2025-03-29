import subprocess

# Gather information on the product 
title = input("What is the the item (Title)? ")
description = input("What is the description? ")
price = input("What is the price? ")
sellers_name= input("What is the sellers name? (If applicable) ")

prompt = title + " " + description + " " + "$" + price + " " + sellers_name

# Open up the bot and feed it the information
run_shark = subprocess.run(['ollama', 'run', 'shark', prompt], capture_output=True, text=True)
sharks_response = run_shark.stdout.strip()  

run_douche = subprocess.run(['ollama', 'run', 'douche', prompt], capture_output=True, text=True)
douches_response = run_douche.stdout.strip()  

print(sharks_response)
print(douches_response)