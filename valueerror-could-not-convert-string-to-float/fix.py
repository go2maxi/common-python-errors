value = "abc"

if value.replace('.', '', 1).isdigit():
    number = float(value)
    print(number)
