import os

file_path = "data.txt"

# Ensure it's a file, not a directory
if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
else:
    print("Expected a file, but got a directory or missing file.")
