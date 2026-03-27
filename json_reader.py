import json

data = {
    "name": "Kazi",
    "course": "CSE AI/ML",
    "year": 1
}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)

print("Data from JSON:", loaded)
