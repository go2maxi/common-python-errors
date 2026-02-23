# Safe handling of potential KeyError

response = {
    "user": {
        "name": "Alice"
    }
}

# 1. Using if-check
if "age" in response["user"]:
    age = response["user"]["age"]
else:
    age = None

print("Using if-check:", age)


# 2. Using .get() (more Pythonic)
age = response["user"].get("age", None)

print("Using .get():", age)
