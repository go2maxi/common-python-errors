# TypeError: 'NoneType' object is not subscriptable

## Reproduce

```python
tags = None  # function returned None

print(tags[0])
```

## Error Message

```
TypeError: 'NoneType' object is not subscriptable
```


## Fix

```python
tags = ["python", "error"]

print(tags[0])
```

## Reflection

I expected a list, but the value was None.


