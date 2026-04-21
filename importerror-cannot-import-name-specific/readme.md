# ImportError: cannot import name 'squareroot' from 'math'

Occurs when trying to import a name that does not exist in the module.

## Reproduce

```python
from math import squareroot

print(squareroot(4))
```

## Error Message

```
ImportError: cannot import name 'squareroot' from 'math'
```

## Fix

```python
from math import sqrt

print(sqrt(4))
```

## Reflection

I tried to import a function with the wrong name. The module exists, but the specific function does not.
 