# ModuleNotFoundError: No module named 'pandas'

Occurs when importing a module that is not installed.

## Reproduce

```python
import pandas as pd

data = [1, 2, 3]
df = pd.DataFrame(data)

print(df)
```

## Error Message

```
ModuleNotFoundError: No module named 'pandas'
```

## Fix

```python
data = [1, 2, 3]

print(data)
```

## Reflection

Used a library without checking if it was installed.
