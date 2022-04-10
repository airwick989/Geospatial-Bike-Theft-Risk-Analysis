import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster

df = pd.read_csv (r"processed_data.csv")

#-------------------------------------------------------------HEATMAP----------------------------------------------------------------------------#

map = folium.Map(location=[43.728136,-79.384666], zoom_start=11)
cluster = MarkerCluster().add_to(map)

for lat,long in zip(df['latitude'], df['longtitude']):
     folium.Marker([lat, long]).add_to(cluster)

max_score = df['score'].max()

lat = df['latitude']
long = df['longtitude']
weight = df['score']

data = []

for i in range(0, len(weight)):
    data.append([lat[i], long[i], weight[i]])

HeatMap(data).add_to(map)

map.save("heatmap.html")