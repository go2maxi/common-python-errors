# IndexError: list assignment index out of range

## Reproduce

```python
numbers = []
numbers[0] = 1
```

## Error message

```
IndexError: list assignment index out of range
```

## Fix.py

```python
numbers = []
numbers.append(1)
print(numbers)
```

## Reflection

Tried to assign to an index that does not exist.


## Reference

- Related case: <https://pyai.io/en/python/basic/lists/>
