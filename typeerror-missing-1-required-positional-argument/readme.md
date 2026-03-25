# TypeError: missing 1 required positional argument

Occurs when a function is called without required arguments.

## reproduce.py

```python
def greet(name):
    print("Hello", name)

greet()
```

## Error Message

```
TypeError: greet() missing 1 required positional argument: 'name'
```

## Fix

```python
def greet(name):
    print("Hello", name)

greet("Python")
```

## Reflection

Called the function without the required argument.
