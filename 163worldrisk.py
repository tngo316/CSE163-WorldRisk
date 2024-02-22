import csv
import pandas as pd

wri_df = pd.read_csv("Users/tonyngo/Downloads/world_risk_index.csv")
top_5 = wri_df.head()
print(top_5)