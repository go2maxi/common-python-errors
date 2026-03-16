# TypeError: 'int' object is not callable

I tried to use the built-in `sum()` function, but it failed because I accidentally overwrote it with a variable.

## reproduce.py

```python
sum = 10
sum(1, 2)
```

## Error message

```
TypeError: 'int' object is not callable
```

## fix.py

```python
total_sum = 10

numbers = [1, 2]
print(sum(numbers))
```

I changed the variable name so it doesn't override the built-in function.
