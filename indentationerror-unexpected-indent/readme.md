# IndentationError: unexpected indent

I added an extra indentation level that Python did not expect.

## reproduce.py

```python
def greet():
    print("Hello")

        print("Welcome")
```

## Error message

```
IndentationError: unexpected indent
```

## fix.py

```python
def greet():
    print("Hello")
    print("Welcome")

greet()
```

I fixed the problem by aligning the indentation correctly.

Reflection: In Python, indentation is not just formatting — it defines code blocks. I also learned to avoid mixing tabs and spaces.