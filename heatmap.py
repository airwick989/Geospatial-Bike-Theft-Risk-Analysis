from operator import index
import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster
from os import system as sys

df = pd.read_csv (r"bicycle_shop_coordinates.csv")

predata = {
    'hood_id': [],
    'number of bike shops': []
}

hood_store_count = {}
for hood in df['hood_id']:
    if hood not in hood_store_count:
        hood_store_count[hood] = 1
    else:
        hood_store_count[hood] += 1


df = df.drop_duplicates(subset='hood_id')
df.reset_index(drop=True, inplace=True)

for key, value in hood_store_count.items():
  predata['hood_id'].append(key)
  predata['number of bike shops'].append(value)

df_revised = pd.DataFrame(predata)

df_revised['latitude'] = df['latitude']
df_revised['longtitude'] = df['longtitude']

#Now add number of bike thefts per hood_id, could also add name for each hood_id

theft_data = pd.read_csv (r"bicycle_thefts.csv") 

predata['bike_thefts'] = [0]*len(predata['hood_id'])

index= 0
for hood_id in theft_data['Hood_ID']:
    try:
        theft_data['Hood_ID'][index] = int(hood_id)
    except Exception:
        theft_data.drop(df.index[index])
        index += 1
        continue

    #print(f"value:{theft_data['Hood_ID'][index]}, type:{type(theft_data['Hood_ID'][index])}")
    if int(hood_id) in predata['hood_id']:
        i = predata['hood_id'].index(int(hood_id))
        predata['bike_thefts'][i] += 1

df_revised['bike_thefts'] = predata['bike_thefts']
predata['score'] = [0]*len(predata['hood_id'])

for i in range(0, len(predata['hood_id'])):
    score = predata['bike_thefts'][i] / predata['number of bike shops'][i]
    predata['score'][i] = round(score ,2)

df_revised['score'] = predata['score']

#-------------------------------------------------------------HEATMAP----------------------------------------------------------------------------#

map = folium.Map(location=[43.728136,-79.384666], zoom_start=11)
cluster = MarkerCluster().add_to(map)

for lat,long in zip(df_revised['latitude'], df_revised['longtitude']):
     folium.Marker([lat, long]).add_to(cluster)

max_score = df_revised['score'].max()

lat = df_revised['latitude']
long = df_revised['longtitude']
weight = df_revised['score']

data = []

for i in range(0, len(weight)):
    data.append([lat[i], long[i], weight[i]])

HeatMap(data).add_to(map)

map.save("heatmap.html")
#sys('cls')