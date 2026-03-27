students = []

while True:
    print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        students.append({"name": name, "age": age})

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        name = input("Enter name to delete: ")
        students = [s for s in students if s["name"] != name]

    elif choice == "4":
        break
