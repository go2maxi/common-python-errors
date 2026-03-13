# ValueError: invalid literal for int()

This error occurs when trying to convert a string to an integer using `int()`
but the string does not contain a valid numeric value.

Example:

int("abc")

Python raises a ValueError because "abc" cannot be interpreted as a number.

## Fix

Use `try-except` to safely handle the error.