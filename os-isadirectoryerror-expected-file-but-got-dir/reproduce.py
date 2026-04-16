import os

# Create a directory
os.makedirs("data_dir", exist_ok=True)

# Trying to open a directory as if it were a file
with open("data_dir", "r") as f:
    content = f.read()
