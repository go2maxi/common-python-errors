import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Trying to assign 3 values to a column with 2 rows
df["salary"] = [1000, 2000, 3000]

print(df)
