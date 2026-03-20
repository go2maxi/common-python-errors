file_path = "data.txt"

with open(file_path, "w") as f:
    f.write("sample")

with open(file_path, "r") as f:
    print(f.read())
