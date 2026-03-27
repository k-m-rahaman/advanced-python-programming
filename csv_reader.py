import csv

data = [
    ["Name", "Age"],
    ["Kazi", 19],
    ["Rahaman", 20]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
