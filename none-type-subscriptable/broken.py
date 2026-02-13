def fetch_user():
    # Simulating API failure (returns None)
    return None

user = fetch_user()

# This line raises:
# TypeError: 'NoneType' object is not subscriptable
print(user["name"])
