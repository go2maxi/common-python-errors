# ValueError: too many values to unpack

## Reproduce

```python
data = [1, 2, 3]

a, b = data
```

## Error Message

ValueError: too many values to unpack (expected 2)

## Fix

```python
data = [1, 2, 3]

a, b, c = data
```

## Reflection

I expected two values but the list had more.
