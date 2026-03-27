while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No tasks found.")

    else:
        break
