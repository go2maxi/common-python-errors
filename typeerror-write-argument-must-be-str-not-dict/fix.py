import json

data = {
    "name": "john",
    "age": 30
}

with open("output.txt", "w") as file:
    file.write(json.dumps(data))
