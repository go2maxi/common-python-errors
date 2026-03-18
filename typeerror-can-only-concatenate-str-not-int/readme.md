# TypeError: can only concatenate str (not "int") to str

## reproduce.py

```python
text = "Hello"
result = text + 1
print(result)
```

## Error message

```
TypeError: can only concatenate str (not "int") to str
```

## fix.py

```python
text = "Hello"
result = text + str(1)
print(result)
```

## Reflection

Convert the integer to a string before concatenation.

```


## Reference

- Related case: [https://pyai.io/en/python/basic/strings/](https://pyai.io/en/python/basic/strings/)

