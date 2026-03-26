# TypeError: unsupported operand type(s) for +: 'int' and 'list'

Occurs when trying to add an integer and a list.

## reproduce.py

```python
my_number = 10
my_list = [1, 2]

print(my_number)
result = my_number + my_list
print(result)
```

## Error Message

```
TypeError: unsupported operand type(s) for +: 'int' and 'list'
```

## Fix

```python
my_number = 10
my_list = [1, 2]

print(my_number)
result = my_number + sum(my_list)
print(result)
```

## Reflection

Thought I could add a list directly to a number.
