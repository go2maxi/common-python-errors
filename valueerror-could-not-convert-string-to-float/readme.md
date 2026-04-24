# ValueError: could not convert string to float

Occurs when a string cannot be converted to a float.

## Reproduce

```python
value = "abc"
number = float(value)
```

## Error Message

```
Traceback (most recent call last):
  File "reproduce.py", line 2, in <module>
    number = float(value)
ValueError: could not convert string to float: 'abc'
```

## Fix

```python
value = "12.3"
number = float(value)
print(number)
```

## Output

```
12.3
```


## Reflection

float() only works with numeric strings.
