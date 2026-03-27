contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ")
        print("Phone:", contacts.get(name, "Not found"))

    else:
        break
