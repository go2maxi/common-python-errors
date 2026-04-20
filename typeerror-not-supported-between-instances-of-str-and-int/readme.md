# TypeError: '>' not supported between instances of 'str' and 'int'

Occurs when comparing a string with an integer.

## Reproduce

```python
age = input("Enter your age: ")

if age > 18:
    print("Allowed")
```

## Error Message

```
Enter your age: 20
Traceback (most recent call last):
  File "reproduce.py", line 3, in <module>
    if age > 18:
       ^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

## Fix

```python
age = int(input("Enter your age: "))

if age > 18:
    print("Allowed")
```

## Reflection

I thought entering a number would be treated as a number, but input() always returns a string. Converting it to int fixed the issue.
