# TypeError: string indices must be integers

## Reproduce

```python
text = "hello"

idx = "1"
print(text[idx])
```

## Error message

TypeError: string indices must be integers, not 'str'

```

## Fix

```python
text = "hello"

idx = int("1")
print(text[idx])
```

## Reflection

I passed a string variable as an index without realizing it.


## Reference

- Related case: <https://pyai.io/en/python/basic/strings/>

