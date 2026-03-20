# UnboundLocalError: local variable referenced before assignment

## Reproduce

```python
count = 10

def update():
    count = count + 1

update()
```

## Error Message

UnboundLocalError: local variable 'count' referenced before assignment

```

## Fix

```python
count = 10

def update():
    global count
    count = count + 1

update()
print(count)
```

## Reflection

I tried to update a variable inside a function without declaring it.


## Reference

- Related case: <https://pyai.io/en/python/basic/functions/>
