from re import I
import pandas as pd
import json

df = pd.read_csv (r"bicycle_shop_coordinates.csv")

predata = {
    'hood_id': [],
    'number of bike shops': []
}

hoodlist = {}
for hood in df['hood_id']:
    if hood not in hoodlist:
        hoodlist[hood] = 1
    else:
        hoodlist[hood] += 1


df = df.drop_duplicates(subset='hood_id')
df.reset_index(drop=True, inplace=True)

for key, value in hoodlist.items():
  predata['hood_id'].append(key)
  predata['number of bike shops'].append(value)

df2 = pd.DataFrame(predata)

df2['latitude'] = df['latitude']
df2['longtitude'] = df['longtitude']

print(df2)  #Now add number of bike thefts per hood_id, could also add name for each hood_id