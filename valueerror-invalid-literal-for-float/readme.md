# ValueError: could not convert string to float

Occurs when converting a non-numeric string to float.

## Reproduce

```python
value = "abc"
number = float(value)
print(number)
```

## Error Message

```
ValueError: could not convert string to float: 'abc'
```

## Fix

```python
value = "3.14"
number = float(value)
print(number)
```

## Reflection

Tried converting a string that wasn't a number.
