# KeyError: 'salary'

Occurs when trying to access a column that does not exist in a DataFrame.

## Reproduce

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

print(df["salary"])
```

## Error Message

```
KeyError: 'salary'
```

## Fix

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Access an existing column
print(df["age"])
```

## Reflection

Assumed the column existed, but it wasn’t in the DataFrame. Spent time checking the data source before verifying the actual column names.
