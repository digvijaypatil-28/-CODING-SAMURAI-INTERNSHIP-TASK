def load_tasks(filename='tasks.txt'):
    try:
        with open(filename, "r") as file:
            return[line.strip()for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:            
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}") 

def main():
    tasks = load_tasks()

    while True:
        print("\n ---TO-DO LIST APPLICATION---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Save and Exit")

        choice= input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"Task '{task}' added.")

        elif choice == "3":
            display_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed= tasks.pop(task_num - 1)
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")   
        
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()                                