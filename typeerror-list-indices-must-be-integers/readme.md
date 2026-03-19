# TypeError: list indices must be integers or slices, not str

## Reproduce

```python
numbers = [10, 20, 30]
print(numbers["1"])
```

## Error Message

```
TypeError: list indices must be integers or slices, not str
```

## Fix

```python
numbers = [10, 20, 30]
index = int("1")
print(numbers[index])
```

## Reflection
Used a string instead of an integer index.


## Reference
- Related case: <https://pyai.io/en/python/basic/lists/>


