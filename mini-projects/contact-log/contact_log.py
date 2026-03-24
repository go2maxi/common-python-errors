contacts = [
    {"name": "user_1", "phone": "0000000000", "location": ["city_a", "district_1"]},
    {"name": "user_2", "phone": "1111111111", "location": ["city_a", "district_2"]},
    {"name": "user_3", "phone": "2222222222", "location": ["city_b", "district_1"]},
]

grouped = {}

for contact in contacts:
    city = contact["location"][0]
    
    if city not in grouped:
        grouped[city] = []
    
    grouped[city].append(contact["name"])

print(grouped)
