# ParserError: Error tokenizing data

Occurs when reading a CSV file with inconsistent delimiters or malformed rows.

## Reproduce

```python
import pandas as pd

# Pandas uses ',' as default delimiter.
# This file uses ';' and has a malformed row at the end.
df = pd.read_csv("data.csv")
print(df)
```

## Error Message

```
ParserError: Error tokenizing data. Expected 1 fields in line 3, saw 2
```

## Fix

```python
import pandas as pd

# Specify the correct delimiter to handle the structure.
df = pd.read_csv("data.csv", delimiter=";")
print(df)
```

## Reflection

File looked fine at first, but one row had an extra value which broke the parsing. Spent time checking column structure before noticing the inconsistent delimiter.
