# NameError: name '...' is not defined

I ran into this error while testing a small Python example.

At first I thought it might be a syntax issue, but it turned out I was trying to use a variable that wasn't defined yet.


Error message:

```
NameError: name 'total' is not defined
```

## What happened

Python tried to use a variable that had not been defined yet.

Example:

```python
x = 10
y = 20

print(total)