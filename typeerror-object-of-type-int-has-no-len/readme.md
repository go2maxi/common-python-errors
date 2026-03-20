# TypeError: object of type 'int' has no len()

## Reproduce

```python
value = 100

length = len(value)
```

## Error Message

TypeError: object of type 'int' has no len()


## Fix

```python
value = 100

length = len(str(value))
```

## Reflection

I tried to use len() on an integer.


## Reference

Related case: <https://pyai.io/en/python/basic/builtin-functions/>
