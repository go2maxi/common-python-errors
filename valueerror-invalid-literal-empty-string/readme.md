# ValueError: invalid literal for int() with base 10: ''

Occurs when trying to convert an empty string to an integer.

## Reproduce

```python
age = input("Enter your age: ")

number = int(age)
print(number)
```

## Error Message

```
Enter your age: 
Traceback (most recent call last):
  File "reproduce.py", line 3, in <module>
    number = int(age)
ValueError: invalid literal for int() with base 10: ''
```

## Fix

```python
age = input("Enter your age: ")

if age.strip() == "":
    print("Please enter a number")
else:
    number = int(age)
    print(number)
```

## Reflection

I just pressed enter without typing anything. input() returns an empty string in that case, which cannot be converted to int.

