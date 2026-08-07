tasks = []

while True:
    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 👉 Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # 👉 View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # 👉 Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            try:
                task_no = int(input("Enter task number to delete: "))
                
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # 👉 Exit
    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")