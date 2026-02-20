# Common Python Errors & Defensive Patterns

A structured collection of reproducible Python runtime errors and practical defensive coding patterns.

## 📂 Current Error Cases

### TypeError: 'NoneType' object is not subscriptable

Occurs when attempting to access keys or indexes from a `None` object (e.g., `data['key']` or `data[0]`).

**Details:**
- [Reproduce & Fix](none-type-subscriptable.md)
- (Step-by-step explanation not available in this repo)

---

### IndexError: list index out of range

Occurs when a list element is accessed with an invalid index.

**Details:**
- [Reproduce & Fix](typeerror-list-indices-must-be-integers-not-str.md)
- (Detailed explanation not included in this repo)

---

### IndexError: tuple index out of range

Occurs when a tuple element is accessed with an invalid index.

**Details:**
- [Reproduce & Fix](indexerror-tuple-index-out-of-range.md)
- (Detailed explanation not included in this repo)

---

## 📖 Related Reference

- [Handling Exceptions and Defensive Programming](https://pyai.io/en/python/basic/handling-exceptions/) — A useful reference on pyai.io
