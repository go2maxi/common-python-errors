# TypeError: can only concatenate str (not "int") to str

## Reproduce

```python
a = "10"
b = 5
print(a + b)
```

## Error message

```
TypeError: can only concatenate str (not "int") to str
```

## Fix

```python
a = "10"
b = 5
print(int(a) + b)
```

## Reflection
Tried to add a string and an integer.


## Reference
- Related case: <https://pyai.io/en/python/basic/strings/>

