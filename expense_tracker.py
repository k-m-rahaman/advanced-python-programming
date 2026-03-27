expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total\n4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        print("Total Expense:", sum(expenses))

    else:
        break
