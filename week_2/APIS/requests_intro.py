# can be used for web scraping, but beautifulsoup is better really
import requests
import json
from pprint import pprint
# this is actually what our browser does.
# sends a get request, server receives it
'''# and responds with an http response

r = requests.get("http://www.bbc.com")
'''#print(type(r.headers))
#print(r.headers["Date"])
'''

if r.status_code == 200:
    # the html file!
    content = r.content
    # python interprets it as text, but it is actually a bytes stream
    print(type(content))'''


#r = requests.get("https://api.postcodes.io/postcodes/SA43AD")

#print(r.headers)

'''if r.status_code == 200:
    content = r.content
    content_json = r.json()
    print(content_json, type(content_json))
    result = content_json["result"]'''

# print the eastings and northings for this postcode

# Dictionary inside a dictionary! 
'''print(content_json["result"]["eastings"])
print(content_json["result"]["northings"])
print(result["northings"])
print(result.get("eastings"))'''

headers = {"Content-Type": "application/json"}
data = {
  "postcodes" : ["OX49 5NU", "M32 0JG", "NE30 1DP"]
}

#could also do json=data (request automatically formats it)
r = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json.dumps(data))

r = r.json()
# puts keys into alphabetical order - (well, for seeing things - 
# dictionaries don't have an order) - (if not otherwise stated)
pprint(r, sort_dicts=False) 
# for each postcode, print POSTCODE: region, parliamentary_constituency

for i in range(0, 3, 1):
    print("---------")
    print(r["result"][i]["query"] + 
          ":\nregion: " + 
          str(r["result"][i]["result"]["region"]) + 
          "\nParliamentary Constituency: " + 
          str(r["result"][i]["result"]["parliamentary_constituency"]))
    if i == 2:
        print("---------")

