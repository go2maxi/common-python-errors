def get_username():
    # Simulating missing data
    return None

username = get_username()

# Defensive pattern 1: explicit check
if username is None:
    print("Username not available")
else:
    parts = username.split("_")
    print(parts)

# Defensive pattern 2: default value
safe_username = username or ""

parts = safe_username.split("_")

print(parts)