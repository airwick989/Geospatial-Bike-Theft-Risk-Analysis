import pandas as pd

df = pd.read_csv (r"bicycle_shop_coordinates.csv")

predata = {
    'hood_id': [],
    'number of bike shops': []
}

#Add stores to list while counting the number of instances a store appears in the same hood
hood_store_count = {}
for hood in df['hood_id']:
    if hood not in hood_store_count:
        hood_store_count[hood] = 1
    else:
        hood_store_count[hood] += 1

#Only keep unique instances of a hood
df = df.drop_duplicates(subset='hood_id')
df.reset_index(drop=True, inplace=True)

for key, value in hood_store_count.items():
  predata['hood_id'].append(key)
  predata['number of bike shops'].append(value)

df_revised = pd.DataFrame(predata)

#Add geodata to revised df
df_revised['latitude'] = df['latitude']
df_revised['longtitude'] = df['longtitude']



theft_data = pd.read_csv (r"bicycle_thefts.csv") 
predata['bike_thefts'] = [0]*len(predata['hood_id'])

#Get number of bike thefts per hood
index= 0
for hood_id in theft_data['Hood_ID']:
    try:
        theft_data['Hood_ID'][index] = int(hood_id)
    except Exception:
        theft_data.drop(df.index[index])
        index += 1
        continue

    if int(hood_id) in predata['hood_id']:
        i = predata['hood_id'].index(int(hood_id))
        predata['bike_thefts'][i] += 1

df_revised['bike_thefts'] = predata['bike_thefts']



#Clean the data
theft_data = theft_data[theft_data.Cost_of_Bike != 0]
theft_data = theft_data[theft_data.Cost_of_Bike != '']
theft_data = theft_data[theft_data.Hood_ID != 'NSA']

#Get average bike cost per hood
bike_costs = (theft_data.groupby(['Hood_ID', 'Cost_of_Bike'], as_index=False).mean().groupby('Hood_ID')['Cost_of_Bike'].mean()).to_frame().T

#Add bike costs to revised dataframe
avg_bike_cost = []
for hood_id in df_revised["hood_id"]:
    avg_bike_cost.append(list(bike_costs[str(hood_id)])[0])

df_revised["average_bicycle_cost"] = avg_bike_cost
predata['average_bicycle_cost'] = df_revised['average_bicycle_cost'].tolist()



predata['score'] = [0]*len(predata['hood_id'])
#Produce scores for each naighborhood
for i in range(0, len(predata['hood_id'])):
    score = predata['bike_thefts'][i]*predata['average_bicycle_cost'][i] / predata['number of bike shops'][i]
    predata['score'][i] = round(score ,2)

df_revised['score'] = predata['score']



#Obtain neighborhood name information
predata['neighborhood'] = []
hood_names = theft_data['NeighbourhoodName'].tolist()
hoodlist = theft_data['Hood_ID'].tolist()
for hood in predata['hood_id']:
    common_index = hoodlist.index(str(hood))
    predata['neighborhood'].append(hood_names[common_index])
df_revised['neighborhood'] = predata['neighborhood']

#Export to CSV
print(df_revised)
# df_revised.to_csv("processed_data.csv")