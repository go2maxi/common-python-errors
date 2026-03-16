# AttributeError: 'list' object has no attribute 'add'

I tried to use the `add()` method on a list, but that method belongs to a set, not a list.

## reproduce.py

```python
numbers = [1, 2, 3]

numbers.add(4)
```

## Error message

```
AttributeError: 'list' object has no attribute 'add'
```

## fix.py

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

I replaced `add()` with `append()`, which is the correct method for lists.

### Reflection
Lists and sets support different methods in Python. I need to check the correct method for each data type before using it.