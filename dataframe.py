import pandas as pd
import json

df = pd.read_csv (r"Automated Speed Enforcement Locations.csv")

latitudes = []
longtitudes = []

i= 0
for coordinate in df["geometry"]:
    placeholder = json.loads(coordinate)
    coordinate = placeholder["coordinates"]
    df["geometry"][i] = coordinate
    latitudes.append(coordinate[1])
    longtitudes.append(coordinate[0])
    i = i+1

df["latitude"] = latitudes
df["longtitude"] = longtitudes

del df['_id']
del df['Location_Code']

coordinates = zip(latitudes, longtitudes)