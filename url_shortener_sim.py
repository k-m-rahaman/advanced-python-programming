import random
import string

url_map = {}

def shorten(url):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short] = url
    return short

def retrieve(short):
    return url_map.get(short, "Not found")

while True:
    print("\n1. Shorten URL\n2. Retrieve URL\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        url = input("Enter URL: ")
        short = shorten(url)
        print("Short URL:", short)

    elif ch == "2":
        code = input("Enter short code: ")
        print("Original URL:", retrieve(code))

    else:
        break