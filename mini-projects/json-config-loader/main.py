import json

with open("config.json", "r") as file:
    config = json.load(file)

print(config)

user_age = config["age"]
print(user_age)

with open("output.txt", "w") as file:
    file.write(config)

value = config["price"]
final = float(value)

print(final)
