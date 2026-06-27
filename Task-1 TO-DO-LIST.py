# Task 1: To-Do List
tasks = []

while True:
    print("\n1. Add a task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        t = input("What do you want to add? ")
        tasks.append(t)
        print("Task added successfully.")
        
    elif choice == '2':
        print("\n--- Your Tasks ---")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])
            
    elif choice == '3':
        task_num = int(input("Enter task number to update: "))
        # simple check to make sure the number exists
        if task_num > 0 and task_num <= len(tasks):
            new_val = input("Enter the new task: ")
            tasks[task_num - 1] = new_val
            print("Task updated.")
        else:
            print("Invalid number!")
            
    elif choice == '4':
        print("Bye!")
        break
        
    else:
        print("Wrong choice, try again.")