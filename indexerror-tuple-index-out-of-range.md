# IndexError: tuple index out of range

```
IndexError: tuple index out of range
```

This error occurs when you try to access a tuple position that does not exist.  
Tuples, like lists, use zero-based indexing.

---

## Example (Reproducing the Error)

```python
values = (10, 20, 30)
print(values[3])
```

The tuple contains three elements.  
Valid indexes are 0, 1, and 2.  
Index 3 is out of range.

---

## Why This Happens

Tuples follow the same indexing rules as lists:

- Indexing starts at 0
- The maximum valid index is length - 1

Even though tuples are immutable, their indexing behavior is identical to lists.

If you're unsure about tuple behavior compared to lists, review the [tuples and ranges tutorial on pyai.io](https://pyai.io/en/python/basic/tuples-ranges/).

---

## Defensive Pattern

Always check boundaries before accessing a tuple:

```python
values = (10, 20, 30)
index = 3

if index < len(values):
    print(values[index])
else:
    print("Index out of range")
```

---

## Related List and Tuple Index Errors

- [IndexError: list index out of range](indexerror-list-index-out-of-range.md)
- [TypeError: list indices must be integers or slices, not str](typeerror-list-indices-must-be-integers-not-str.md)

---

If you'd like a broader explanation of list index errors, see the main guide:

- [IndexError: list index out of range](indexerror-list-index-out-of-range.md)


