# AttributeError: 'NoneType' object has no attribute 'append'

## Reproduce

```python
data = None
data.append("new item")
```

## Error Message

```
AttributeError: 'NoneType' object has no attribute 'append'
```

## Fix

```python
data = []

data.append("new item")
```

## Reflection
Tried to call append on None.


## Reference
- Related case: <https://pyai.io/en/python/basic/lists/>
