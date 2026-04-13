import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Match the number of rows
df["salary"] = [1000, 2000]

print(df)
