# IndexError: string index out of range

Occurs when accessing a character outside the string length.

## Reproduce

```python
text = "hi"

print(text)
char = text[5]
print(char)
```

## Error Message

```
IndexError: string index out of range
```

## Fix

```python
text = "hi"

print(text)
if len(text) > 5:
    char = text[5]
    print(char)
```

## Reflection

Ended up accessing an index that didn’t exist.


## Reference

- Related case: <https://pyai.io/en/python/basic/strings/>
