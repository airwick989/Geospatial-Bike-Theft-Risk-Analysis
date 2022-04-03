import pandas as pd
import json

bicycle_shop_coordinates_du = open("bicycle_shop_coordinates.csv", "w")

data = json.load(open("FoursquareData.json", "r"))
for i in data["results"]:
    lat = i["geocodes"]["main"]["latitude"]
    lon = i["geocodes"]["main"]["longitude"]
    bicycle_shop_coordinates_du.write(f"{lat},{lon}")
    bicycle_shop_coordinates_du.write("\n")
