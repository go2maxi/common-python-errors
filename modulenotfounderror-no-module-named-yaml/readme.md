# ModuleNotFoundError: No module named 'yaml'

Occurs when importing a module that is not installed.

## Reproduce

```python
import yaml

data = {"name": "john"}
print(data)
```

## Error Message

```
ModuleNotFoundError: No module named 'yaml'
```

## Fix

```python
data = {"name": "john"}
print(data)
```

## Reflection

Tried importing a module without checking if it was available.
