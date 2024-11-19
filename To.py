def main():
    tasks = []  # The list to store tasks

    while True:
        print("\n--To do List--")
        print("1. Add Some task")
        print("2. Show task")
        print("3. Mark as done")
        print("4. Exit")

        choice = int(input("Enter your choice: "))  # Get the user input

        if choice == 1:  # Add tasks
            print()
            n_tasks = int(input("How many tasks do you want to enter? "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})  # Correct task structure
                print("Task added successfully!")

        elif choice == 2:  # Show tasks
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == 3:  # Mark a task as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == 4:  # Exit
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Call the main function to run the program
