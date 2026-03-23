# TypeError: unsupported operand type(s) for +: 'int' and 'str'

## Reproduce

```python
a = 10
b = "5"

result = a + b
print(result)
```

## Error Message

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

## Fix

```python
a = 10
b = "5"

result = a + int(b)
print(result)
```

## Reflection

I mixed types without noticing and tried to add them directly.
