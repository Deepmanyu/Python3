# Query string 

#What is a query string
# a way to passs data to the server as a part of a GET request
# http://www.example.com/?key1=value1&key2=value2 - look at the key value
# pairs

# some example of keys
# q = query 
# oq = original query

import requests 
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES: API CALL BY DEEP")
header_colored = colored(header, color = "red") 

print(header_colored)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers = {"Accept": "application/json"},
	params = {"term": user_input}
).json()

num_jokes = res["total_jokes"] 
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one: ")
	print(choice(results)["joke"]) 
elif num_jokes == 1:
	print(f"I found 1 joke about {user_input}")
	print(results[0]["joke"])
else:
	print(f"Sorry could not find a joke about: {user_input}")


