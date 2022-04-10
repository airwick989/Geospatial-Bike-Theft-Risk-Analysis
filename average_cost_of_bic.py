import pandas as pd

df1 = pd.read_csv("bicycle_thefts.csv")
df2 = pd.read_csv("cluster_data.csv")

df1 = df1[df1.Cost_of_Bike != 0]
df1 = df1[df1.Cost_of_Bike != '']
df1 = df1[df1.Hood_ID != 'NSA']


df3 = (df1.groupby(['Hood_ID', 'Cost_of_Bike'], as_index=False).mean().groupby('Hood_ID')['Cost_of_Bike'].mean()).to_frame().T

print(df3)
avg_bike_cost = []
for hood_id in df2["hood_id"]:
    print(f"{hood_id} {list(df3[str(hood_id)])}")
    avg_bike_cost.append(list(df3[str(hood_id)])[0])


df2["average_bicycle_cost"] = avg_bike_cost

print(df2.head())

df2.to_csv("cluster_data_updated.csv")
# for hood_id in df2["hood_id"]:



# for hood_id_in_cluster_data_csv in df2["hood_id"]:
#     index = 0
#     for hood_id in df1["Hood_ID"]:
#         print(hood_id)
#         index += 1