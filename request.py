import requests

url = "https://api.foursquare.com/v3/places/search?query=coffee&near=toronto&limit=10"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq37aiTLwAGMwc0LBG0ob2Sb22qNqfeOzO1G7w624eeVfc="
}

response = requests.request("GET", url, headers=headers)

print(response.text)