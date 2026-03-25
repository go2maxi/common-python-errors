# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 0: invalid start byte

Occurs when trying to read a file with the wrong encoding (e.g., reading CP949/ANSI as UTF-8).

test.txt exists and is encoded in cp949..


## reproduce.py

```python
# test.txt is encoded in cp949 (ANSI)
with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
```

## Error Message

```
Traceback (most recent call last):
  File "reproduce.py", line 3, in <module>
    data = f.read()
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 0: invalid start byte
```

## Fix

```python
with open('test.txt', 'r', encoding='cp949') as f:
    data = f.read()
    print(data)
```

Reflection

File encoding was different than I expected.

