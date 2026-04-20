# ModuleNotFoundError: No module named 'my_utils'

Occurs when trying to import a local module that Python cannot find.

## Reproduce

```python
from my_utils import greet

greet()
```

## Error Message

```
ModuleNotFoundError: No module named 'my_utils'
```

## Fix

```python
# Make sure my_utils.py exists in the same directory

from my_utils import greet

greet()
```

## Reflection

I thought the file was there, but it turned out Python couldn't see it. In my case, the file was either missing or not in the same folder as the script.
