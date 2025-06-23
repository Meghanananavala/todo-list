def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet!")

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue

            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: "))
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid input.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if _name_ == "_main_":
    main()