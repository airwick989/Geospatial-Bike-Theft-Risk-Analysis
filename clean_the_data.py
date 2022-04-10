import pandas as pd

df = pd.read_csv ('bicycle_thefts.csv').copy()
print(df.head())


filtered_df = df[["Hood_ID", "NeighbourhoodName", "City", "Premises_Type"]].copy()

print(filtered_df.head(50))



filtered_df.to_csv("filtered_bicycle_thefts.csv")
