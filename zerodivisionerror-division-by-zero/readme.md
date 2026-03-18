# ZeroDivisionError: division by zero

Occurs when attempting to divide a number by zero.

## reproduce.py

```python
a = 10
b = 0
print(a / b)
```

## Error message

```
ZeroDivisionError: division by zero
```

## fix.py

```python
a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")
```

## Reflection

Ensure the divisor is not zero before performing division.
