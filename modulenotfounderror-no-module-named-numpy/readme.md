# ModuleNotFoundError: No module named 'numpy'

Occurs when trying to import a module that is not installed.

## Reproduce

```python
import numpy as np

print(np.array([1, 2, 3]))
```

## Error Message

```
ModuleNotFoundError: No module named 'numpy'
```

## Fix

```python
pip install numpy
```

## Reflection

Tried to use a module before installing it.
