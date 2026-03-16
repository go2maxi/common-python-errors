# ModuleNotFoundError: No module named 'requests'

I tried to import the `requests` library, but Python could not find the module because it was not installed.

## reproduce.py

```python
import requests
```

## Error message

```
ModuleNotFoundError: No module named 'requests'
```

## fix.py

```python
# pip install requests
import requests
```

If the package is installed correctly, the import statement will work.

Note: If you later make network requests using the library, you may encounter SSL or connection errors depending on your system environment. Those are environment-related issues and are separate from the `ModuleNotFoundError`.