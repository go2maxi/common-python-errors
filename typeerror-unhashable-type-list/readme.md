# TypeError: unhashable type: 'list'

## Reproduce

```python
contacts = {}

member = ["John", "London"]
contacts[member] = "555-1234"
```

## Error Message

```
TypeError: unhashable type: 'list'
```

## Fix

```python
contacts = {}

member = ("John", "London")
contacts[member] = "555-1234"
```

## Reflection

Used a list as a dictionary key.


## Reference

- Related case: <https://pyai.io/en/python/basic/dictionaries/>


## Related Context
- Hit this while grouping contacts by location
