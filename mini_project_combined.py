tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Save Tasks\n4. Load Tasks\n5. Exit")
    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for t in tasks:
            print("-", t)

    elif choice == "3":
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print("Tasks saved!")

    elif choice == "4":
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.read().splitlines()
            print("Tasks loaded!")
        except FileNotFoundError:
            print("No saved tasks found.")

    else:
        break