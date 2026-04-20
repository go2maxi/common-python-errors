import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data.txt")

with open(file_path, "r") as f:
    content = f.read()

print(content)
