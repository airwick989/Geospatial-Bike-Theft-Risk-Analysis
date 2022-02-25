import pandas as pd
import folium
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

venues_map = folium.Map(location=[43.728136,-79.384666], zoom_start=11)

for lat, lng, label in zip(latitudes, longtitudes, df["location"]):

    label = f"{label} \n{lat},{lng}"

    folium.features.CircleMarker(
        [lat, lng],
        radius=5,
        color='blue',
        popup=label,
        fill = True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(venues_map)

venues_map.save("map.html")
