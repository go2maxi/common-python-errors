# IndexError: list index out of range

```
IndexError: list index out of range
```

If you're seeing this error, it means your code is trying to access a list position that does not exist.  
In Python, lists use zero-based indexing, which means the first element starts at index 0.

---

## Quick Example (Reproducing the Error)

```python
numbers = [10, 20, 30]
print(numbers[3])
```

This raises an error because the list has only three elements.  
Valid indexes are 0, 1, and 2. Index 3 does not exist.

### Quick Fix

Make sure the index is smaller than the length of the list:

```python
numbers = [10, 20, 30]

if 3 < len(numbers):
    print(numbers[3])
```

---

## Why This Happens

### Zero-Based Indexing

In Python, indexing starts at 0.

If a list has 3 elements:

```python
numbers = [10, 20, 30]
```

The valid indexes are:

- 0
- 1
- 2

The length of the list is 3, but the highest valid index is 2.

Trying to access index 3 causes:

```
IndexError: list index out of range
```

---

### Common Loop Mistake (Off-by-One Error)

A very common real-world mistake happens inside loops.

```python
numbers = [10, 20, 30]

for i in range(len(numbers) + 1):
    print(numbers[i])
```

The problem is `+ 1`.

`range(len(numbers))` already produces correct indexes:

- 0
- 1
- 2

Adding `+ 1` forces the loop to attempt index 3, which does not exist.

Correct version:

```python
for i in range(len(numbers)):
    print(numbers[i])
```

---

## Defensive Patterns

### 1) Boundary Check

If the index may vary, always check the boundary:

```python
numbers = [10, 20, 30]
index = 3

if index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range")
```

This approach works well when the index value is predictable.

---

### 2) Using try/except

In cases where the index depends on dynamic input, structured exception handling is safer:

```python
numbers = [10, 20, 30]

try:
    print(numbers[3])
except IndexError:
    print("Handled safely")
```

Beyond manual boundary checks, structured exception handling becomes important when working with user input or dynamic data sources.

For a more detailed explanation of structured exception handling in Python, see the [handling exceptions tutorial on pyai.io](https://pyai.io/en/python/basic/handling-exceptions/).

---

## Related List and Tuple Index Errors

- [TypeError: list indices must be integers or slices, not str](typeerror-list-indices-must-be-integers-not-str.md)
- [IndexError: tuple index out of range](indexerror-tuple-index-out-of-range.md)
