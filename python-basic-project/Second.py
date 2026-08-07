tasks = []

while True:
    print("This is todo application.")
    print("==== Here you can add, view, delete the tasks. ====")
    print("Please select the option from below:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("===============================================")

    userChoice = int(input("Enter your choice: "))

    if userChoice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully! \n")
        print("===============================================")

    elif userChoice == 2:
        taskCount = len(tasks)
        if taskCount == 0:
            print("No tasks available! \n")
            print("===============================================")
        else:
            print("Your tasks:")
            for i in range(taskCount):
                print(f"{i + 1}. {tasks[i]}")
            print("===============================================")

    else:
        print("Invalid choice! Please select a valid option.")
        exit()
    