# Handling ValueError with try-except
value = "abc"

try:
    number = int(value)
    print(number)
except ValueError:
    print("Cannot convert the string to an integer.")