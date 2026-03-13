# KeyError

## What is KeyError?

A `KeyError` occurs when attempting to access a dictionary key that does not exist.

```python
data = {"name": "Alice"}
print(data["age"])  # KeyError
```

The key `"age"` is not present in the dictionary.

---

## Why this happens in real projects

In real-world applications, a `KeyError` commonly occurs when:

- Handling external API responses.
- Parsing JSON data.
- Processing dynamic user input.
- Assuming optional fields are always present.

Example:

```python
response = {
    "user": {
        "name": "Alice"
    }
}

age = response["user"]["age"]  # KeyError
```

If the external system does not guarantee the `"age"` field, direct indexing becomes unsafe.

---

## How to Fix

### 1. Check existence explicitly

```python
if "age" in response["user"]:
    age = response["user"]["age"]
```

---

### 2. Use `dict.get()`

```python
age = response["user"].get("age")
```

This returns `None` if the key is missing.

You may also provide a default value:

```python
age = response["user"].get("age", 0)
```

---

### 3. Use defaultdict (when aggregation is intended)

```python
from collections import defaultdict

counter = defaultdict(int)
counter["a"] += 1
```

`defaultdict` is useful for counting or grouping patterns.

If the goal is safe lookup rather than aggregation, `dict.get()` is usually clearer and more explicit.

