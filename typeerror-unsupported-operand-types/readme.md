# TypeError: can only concatenate str (not "int") to str

Occurs when trying to add a string and an integer.

## reproduce.py

```python
a = "10"
b = 5
print(a + b)
```

## Error message

```
TypeError: can only concatenate str (not "int") to str
```

## fix.py

```python
a = "10"
b = 5
print(int(a) + b)
```

### Reflection
Ensure operands are of compatible types (e.g., convert using int or str).
