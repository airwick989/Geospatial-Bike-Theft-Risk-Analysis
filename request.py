from textwrap import indent
import requests
import json

url = "https://api.foursquare.com/v3/places/search?ll=43.69%2C-79.33&radius=15000&categories=17119&limit=50"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq37aiTLwAGMwc0LBG0ob2Sb22qNqfeOzO1G7w624eeVfc="
}

response = requests.request("GET", url, headers=headers)

#print(response.text)
data = json.loads(response.text)


with open('FoursquareData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
