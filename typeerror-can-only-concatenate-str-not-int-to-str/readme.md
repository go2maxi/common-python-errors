# TypeError: can only concatenate str (not "int") to str

Occurs when trying to concatenate a string with an integer.

## Reproduce

```python
value = "10"
result = value + 5
print(result)
```

## Error Message

```
TypeError: can only concatenate str (not "int") to str
```

## Fix

```python
value = "10"
result = int(value) + 5
print(result)
```

## Reflection

Mixed string and integer without noticing the type difference.
