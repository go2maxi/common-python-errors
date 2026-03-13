# reproduce.py

data = None

try:
    print("Attempting to access index 0 of NoneType object...")
    print(data[0])
except TypeError as e:
    print(f"Caught expected error: {e}")