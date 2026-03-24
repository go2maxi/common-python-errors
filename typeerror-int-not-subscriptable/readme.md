# TypeError: 'int' object is not subscriptable

Occurs when trying to access an index on a non-sequence type like int.

## reproduce.py

```python
phone_number = 1234567890

print(phone_number[0])
```

## Error Message

```
TypeError: 'int' object is not subscriptable
```

## Fix

```python
phone_number = 1234567890

phone_str = str(phone_number)
print(phone_str[0])
```

## Reflection

Tried to index a number directly. Converting to string fixed it.

## Reference
Related case: <https://pyai.io/en/python/basic/strings/>
