# IndexError: list index out of range

## Reproduce

```python
numbers = [10, 20, 30]
print(numbers[3])
```

## Error Message

```
IndexError: list index out of range
```

## Fix

```python
numbers = [10, 20, 30]
print(numbers[2])
```

## Reflection
Index 3 was out of range.


## Reference
- Related case: <https://pyai.io/en/python/basic/lists/>
