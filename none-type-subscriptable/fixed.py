def fetch_user():
    # Simulating API failure (returns None)
    return None

user = fetch_user()

# Defensive Pattern 1: Explicit check
if user is None:
    print("User not found")
else:
    print(user.get("name"))

# Defensive Pattern 2: Short-circuit evaluation
safe_user = user or {}
print(safe_user.get("name", "Unknown"))
