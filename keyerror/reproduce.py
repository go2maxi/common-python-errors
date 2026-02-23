# Reproducing KeyError using a simulated API response

response = {
    "user": {
        "name": "Alice"
    }
}

# This will raise KeyError because "age" does not exist
age = response["user"]["age"]

print(age)
