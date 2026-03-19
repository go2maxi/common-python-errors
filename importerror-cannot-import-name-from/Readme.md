# ImportError: cannot import name '...' from '...'


## Reproduce.py

```python
from math import something
```


## Error Message

```
ImportError: cannot import name 'something' from 'math'
```


## Fix.py

```python
from math import sqrt
```


## Reflection
Tried to import something that doesn't exist.


## Reference
- Related case: <https://pyai.io/en/python/basic/modules-packages/>

