# TypeError: string indices must be integers

## reproduce.py

```python
text = "hello"
print(text["0"])
```

## error message

TypeError: string indices must be integers

```

## fix.py
```python
text = "hello"
print(text[0])
```

## reflection

"0" was the problem, not 0.

```

## Reference

- Related case: [https://pyai.io/en/python/basic/strings/](https://pyai.io/en/python/basic/strings/)

