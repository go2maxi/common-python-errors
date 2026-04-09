import pandas as pd

df = pd.read_csv("data_utf16.csv", encoding="utf-16")
print(df.head())
