# ValueError: Length of values does not match length of index

Occurs when assigning a list or array whose length does not match the DataFrame index.

## Reproduce

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Trying to assign 3 values to a column with 2 rows
df["salary"] = [1000, 2000, 3000]

print(df)
```

## Error Message

```
ValueError: Length of values does not match length of index
```

## Fix

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Match the number of rows
df["salary"] = [1000, 2000]

print(df)
```

## Reflection

Tried to assign more values than rows in the DataFrame. Spent time checking the data before realizing the length mismatch.
