import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Trying to access a row that does not exist
print(df.iloc[5])
