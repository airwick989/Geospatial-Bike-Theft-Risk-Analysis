import pandas as pd
import json
from shapely.geometry import shape, Point

bicycle_shop_coordinates_du = open("bicycle_shop_coordinates.csv", "w")

points_with_hood_id = [] 

data = json.load(open("FoursquareData.json", "r"))
for i in data["results"]:
    lat = i["geocodes"]["main"]["latitude"]
    lon = i["geocodes"]["main"]["longitude"]
    points_with_hood_id.append( { "point": Point(lon, lat), "hood_id": None, "lon": lon, "lat": lat } )

with open("Neighbourhoods.json", "r") as f:
    geojs = json.load(f)

for feature in geojs["features"]:
    polygon = shape(feature["geometry"])
    for point in points_with_hood_id:
        print(point["point"])
        if polygon.contains(point["point"]):
            point["hood_id"] = feature["properties"]["AREA_SHORT_CODE"]

for p in points_with_hood_id:
    bicycle_shop_coordinates_du.write(f"{p['lat']},{p['lon']},{p['hood_id']}")
    bicycle_shop_coordinates_du.write("\n")

