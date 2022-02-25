import requests

url = "https://api.foursquare.com/v3/places/search?ll=43.72%2C-79.57&radius=100000&categories=12057&limit=50"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq37aiTLwAGMwc0LBG0ob2Sb22qNqfeOzO1G7w624eeVfc="
}

response = requests.request("GET", url, headers=headers)

print(response.text)