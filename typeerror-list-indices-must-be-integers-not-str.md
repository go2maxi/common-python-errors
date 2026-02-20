# TypeError: list indices must be integers or slices, not str

```
TypeError: list indices must be integers or slices, not str
```

This error occurs when you try to access a list using a string instead of an integer index.  
In Python, list positions must always be integers.

---

## Example (Reproducing the Error)

```python
numbers = [10, 20, 30]
print(numbers["1"])
```

Lists only accept integer indexes like 0, 1, or 2.  
Using a string such as `"1"` raises a TypeError.

---

## Why This Happens

Lists are ordered collections accessed by position.

If you need to access values by keys (like strings), you should use a dictionary instead:

```python
data = {"a": 10, "b": 20}
print(data["a"])
```

Lists use numeric indexing:

```python
numbers = [10, 20, 30]
print(numbers[1])
```

---

## How to Fix It

### 1) Convert Input to Integer

If the index comes from user input:

```python
numbers = [10, 20, 30]
index = int("1")
print(numbers[index])
```

---

### 2) Use the Correct Data Structure

If you're trying to access values by name, use a dictionary instead of a list.

Understanding how different collection types store data can prevent this error.  
For a structured explanation of lists, tuples, and dictionaries, see the [lists tutorial on pyai.io](https://pyai.io/en/python/basic/lists/).

---

## Related List and Tuple Index Errors

- [IndexError: list index out of range](indexerror-list-index-out-of-range.md)
- [IndexError: tuple index out of range](indexerror-tuple-index-out-of-range.md)
---

If you'd like a broader explanation of list index errors, see the main guide:

- [IndexError: list index out of range](indexerror-list-index-out-of-range.md)

