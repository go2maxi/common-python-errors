# Common Python Errors & Defensive Patterns

A structured collection of reproducible Python runtime errors and practical defensive coding patterns.

## 📂 Current Error Cases

### 1. TypeError: 'NoneType' object is not subscriptable
Occurs when attempting to access keys or indexes from a `None` object.

**Details:**
- [Reproduce & Fix](none-type-subscriptable/explanation.md)

---

### 2. TypeError: list indices must be integers or slices, not str
Occurs when a list is accessed using a string instead of an integer.

**Details:**
- [Reproduce & Fix](typeerror-list-indices-must-be-integers-not-str.md)

---

### 3. IndexError: list index out of range
Occurs when a list element is accessed with an invalid index.

**Details:**
- [Reproduce & Fix](indexerror-list-index-out-of-range.md)

---

### 4. IndexError: tuple index out of range
Occurs when a tuple element is accessed with an invalid index.

**Details:**
- [Reproduce & Fix](indexerror-tuple-index-out-of-range.md)

---

### 5. KeyError
Occurs when accessing a dictionary with a non-existent key.

**Details:**
- [View Explanation](keyerror/explanation.md)


## 📖 Related Reference

- [Handling Exceptions and Defensive Programming](https://pyai.io/en/python/basic/handling-exceptions/) — A useful reference on pyai.io
