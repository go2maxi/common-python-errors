# ValueError: invalid literal for int() with base 10

Occurs when trying to convert a non-numeric string into an integer.

## Reproduce

```python
# reproduce.py
value = "abc"
number = int(value)
```

## Error message

```
Traceback (most recent call last):
  File "reproduce.py", line 2, in <module>
    number = int(value)
ValueError: invalid literal for int() with base 10: 'abc'
```

## fix.py

```python
value = "123"
if value.isdigit():
    number = int(value)
    print(number)
```

## Output

```
123
```

## Reflection
The string "abc" cannot be converted to an integer. Check if the string contains only digits before using int().
