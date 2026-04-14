import os

# create a file
with open("data.txt", "w") as f:
    f.write("hello")

# try to list contents as if it's a directory
os.listdir("data.txt")
