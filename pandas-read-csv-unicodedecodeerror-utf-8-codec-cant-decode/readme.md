# UnicodeDecodeError: 'utf-8' codec can't decode byte

Occurs when reading a file with the wrong encoding.

## Reproduce

```python
import pandas as pd

df = pd.read_csv("data_utf16.csv")
print(df.head())
```

## Error Message
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

## Fix

```python
import pandas as pd

df = pd.read_csv("data_utf16.csv", encoding="utf-16")
print(df.head())
```

## Reflection
Assumed default encoding would work, but file was saved as utf-16. Spent time checking the data structure before identifying the encoding issue.
