import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))

with open("password.txt", "w") as f:
    f.write(password)

print("Password saved to file.")