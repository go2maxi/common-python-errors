# SyntaxError: invalid syntax

## Reproduce

```python
def add_member(name, phone)
    return {"name": name, "phone": phone}
```

## Error Messsge

```
SyntaxError: invalid syntax
````

## Fix

```python
def add_member(name, phone):
    return {"name": name, "phone": phone}
```

## Reflection

Missed a colon after function definition.


## Reference

- Related case: <https://pyai.io/en/python/basic/errors-and-tracebacks/>


## Related Context

- Seen while building a simple contact-log script.
