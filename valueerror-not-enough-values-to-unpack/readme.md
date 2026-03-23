# ValueError: not enough values to unpack (expected 3, got 2)

## Reproduce

```python
data = [1, 2]

a, b, c = data
print(a, b, c)
```

## Error Message

```
ValueError: not enough values to unpack (expected 3, got 2)
```

## Fix

```python
data = [1, 2]

a, b = data
print(a, b)
```

## Reflection

I expected more values than the list actually had.


## Reference

- Related case: <https://pyai.io/en/python/basic/lists/>
