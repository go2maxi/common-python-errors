import json

with open("users.json", "r") as file:
    data = json.load(file)

print(data)

import numpy as np

scores = data["scores"]

print(scores[5])

result = scores + 10

data.append({"new": "user"})
