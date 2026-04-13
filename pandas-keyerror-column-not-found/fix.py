import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

print(df["age"])
