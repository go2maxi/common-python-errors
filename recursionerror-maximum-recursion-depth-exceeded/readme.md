# RecursionError: maximum recursion depth exceeded

Occurs when a recursive function does not have a proper base case and keeps calling itself indefinitely.

## Reproduce

```python
def recursive_function():
    return recursive_function()

recursive_function()
```

## Error Message

```
RecursionError: maximum recursion depth exceeded
```

## Fix

```python
def recursive_function(n):
    if n <= 0:
        return 0
    return recursive_function(n - 1)

print(recursive_function(5))
```

## Reflection

Forgot to add a base case, so the function kept calling itself until Python stopped it.
