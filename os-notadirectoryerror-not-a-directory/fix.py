import os

# create a directory instead
os.makedirs("data_dir", exist_ok=True)

# now list directory
print(os.listdir("data_dir"))

