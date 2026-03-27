books = ["Python", "C Programming", "AI Basics"]

while True:
    print("\n1. View Books\n2. Issue Book\n3. Return Book\n4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print("Available Books:", books)

    elif choice == "2":
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book issued")
        else:
            print("Not available")

    elif choice == "3":
        book = input("Enter book name: ")
        books.append(book)
        print("Book returned")

    else:
        break
