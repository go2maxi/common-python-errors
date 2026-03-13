## What happened

I hit this error when I tried to use `.split()` on a variable that turned out to be `None`.

```python
username = None
username.split("_")
# Raises: AttributeError: 'NoneType' object has no attribute 'split'