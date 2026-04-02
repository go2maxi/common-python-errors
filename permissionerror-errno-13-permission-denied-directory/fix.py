import os

file_path = "data.txt"

with open(file_path, "w") as file:
    file.write("hello")

os.remove(file_path)

