filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        text = f.read()
        words = text.split()
        print("Total words:", len(words))
except FileNotFoundError:
    print("File not found.")
