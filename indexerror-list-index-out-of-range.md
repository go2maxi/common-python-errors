# IndexError: list index out of range

```
IndexError: list index out of range
```

If this error just showed up, it can feel confusing at first. Most of the time, it simply means the code tried to access an index that isn’t actually in the list.

---

## Quick Example (Reproducing the Error)

```python
numbers = [10, 20, 30]
print(numbers[3])
```

This raises an error because the list contains only three elements.  
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

The part that often causes confusion is that Python starts counting from 0, not 1. It sounds simple, but once conditions or loops become slightly complex, it’s easy to miscalculate the final index.

If a list has three elements:

```python
numbers = [10, 20, 30]
```

The valid indexes are:

- 0  
- 1  
- 2  

The length of the list is 3, but the highest valid index is 2.

Trying to access index 3 results in:

```
IndexError: list index out of range
```

---

### Common Loop Mistake (Off-by-One Error)

A very common real-world mistake happens inside loops:

```python
numbers = [10, 20, 30]

for i in range(len(numbers) + 1):
    print(numbers[i])
```

That `+ 1` is usually the cause. It often sneaks in because we’re thinking about the length itself rather than the last valid index.

In most cases, `range(len(numbers))` is enough. If you ever find yourself adding `+ 1`, it’s worth pausing and checking whether the loop really needs it.

`range(len(numbers))` already produces the correct indexes:

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

If the index may vary, check the boundary first:

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

When the index depends on dynamic input, structured exception handling can be safer:

```python
numbers = [10, 20, 30]

try:
    print(numbers[3])
except IndexError:
    print("Handled safely")
```

Beyond manual boundary checks, structured exception handling becomes important when working with user input or dynamic data sources.

If you're exploring how to handle exceptions more gracefully in larger programs, the [handling exceptions tutorial on pyai.io](https://pyai.io/en/python/basic/handling-exceptions/) is one useful reference. Still, the right pattern often depends on your specific context.

---

## Related List and Tuple Index Errors

- [TypeError: list indices must be integers or slices, not str](typeerror-list-indices-must-be-integers-not-str.md)
- [IndexError: tuple index out of range](indexerror-tuple-index-out-of-range.md)
