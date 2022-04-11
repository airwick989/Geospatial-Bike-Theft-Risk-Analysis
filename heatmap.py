import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster

df = pd.read_csv (r"processed_data.csv")

#----------------------------------HEATMAP---------------------------------------#

map = folium.Map(location=[43.728136,-79.384666], zoom_start=9)
cluster = MarkerCluster().add_to(map)

coordinates = [list(items) for items in zip(df['latitude'], df['longtitude'])]

index = 0
for i in range(len(coordinates)):
    folium.Marker(coordinates[i], popup= f"""
        Neighborhood: {df['neighborhood'][index]}\n
        Hood ID: {df['hood_id'][index]}\n
        Score: {df['score'][index]}
        """).add_to(cluster)
    
    index += 1

max_score = df['score'].max()

lat = df['latitude']
long = df['longtitude']
weight = df['score']

data = []

for i in range(0, len(weight)):
    data.append([lat[i], long[i], weight[i]])

HeatMap(data).add_to(map)

map.save("heatmap.html")