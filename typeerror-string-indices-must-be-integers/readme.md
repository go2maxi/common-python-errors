# TypeError: string indices must be integers

## Reproduce.py

```python
text = "hello"
print(text["0"])
```

## Error message

TypeError: string indices must be integers

```

## Fix.py
```python
text = "hello"
print(text[0])
```

## Reflection

"0" was the problem, not 0.


## Reference
- Related case: <https://pyai.io/en/python/basic/strings/>
