# AttributeError: 'tuple' object has no attribute 'append'

## Reproduce

```python
data = (1, 2)
data.append(3)
```

## Error Message

```
AttributeError: 'tuple' object has no attribute 'append'
```

## Fix

```python
data = [1, 2]
data.append(3)
```


## Reflection
Tried to use append on a tuple.


## Reference
- Related case: <https://pyai.io/en/python/basic/lists/>
