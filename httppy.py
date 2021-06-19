# HTTP

import requests

url = "http://www.google.com"
res_1 = requests.get(url)

print(f"your request to {url} came back with status code: {res_1.status_code}")
print(res_1.ok)
print(res_1.headers)
#print(res_1.text) #massive html data would be received. This would be same
# as getting the data form develop and viewing source code


#

url2 = "https://icanhazdadjoke.com/"
#The below would give you the html version of the website
# 
# res_2 = requests.get(url2, headers = {"Accept": "text/html"})
#
# its messy hence we dont use that insted we use the below version
# remember many websites are not made to give this version. Even google
# is not set up to give that and you get the default html version
res_2 = requests.get(url2, headers = {"Accept": "text/plain"})
print(res_2.text)

#Plain text is good but there is another version to get data that is 
# even better. Its JSON. it stands fot javascript object notation.
# Its a data format that python can very quickly convert into python code

res_3 = requests.get(url2, headers = {"Accept": "application/json"})
print(res_3.text) # this looks like a dictionary but its string
print(res_3.json()) #this gives a dictionary

data3 = res_3.json()
print(type(data3))
#As now we know that we have a python dictionary as data3. We can use
# [] to get only the joke

print(data3["joke"] * 5) 

#So remember, if it supports JSON we do a JSON
