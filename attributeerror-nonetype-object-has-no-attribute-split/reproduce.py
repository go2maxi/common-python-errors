def get_username():
    # Simulating missing data
    return None

username = get_username()

# This line raises:
# AttributeError: 'NoneType' object has no attribute 'split'
parts = username.split("_")

print(parts)