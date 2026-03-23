# AttributeError: 'str' object has no attribute 'append'

## Reproduce

```python
text = "hello"
text.append("world")
```

## Error Message

```
AttributeError: 'str' object has no attribute 'append'
```

## Fix

```python
text = "hello"
text = text + "world"

print(text)
```

## Reflection

I treated a string like a list and tried to use append.
