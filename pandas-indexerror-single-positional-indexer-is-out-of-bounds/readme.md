# IndexError: single positional indexer is out-of-bounds

Occurs when trying to access a row or column position that does not exist using iloc.

## Reproduce

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Trying to access a row that does not exist
print(df.iloc[5])
```

## Error Message

```
IndexError: single positional indexer is out-of-bounds
```

## Fix

```python
import pandas as pd

data = {
    "name": ["john", "peter"],
    "age": [30, 25]
}

df = pd.DataFrame(data)

# Access a valid index
print(df.iloc[1])
```

## Reflection

Tried to access an index that was out of range. Didn’t check the DataFrame size before using iloc.

