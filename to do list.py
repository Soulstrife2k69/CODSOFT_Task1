# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task_description = input("Enter task description: ")
    task = {
        "description": task_description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    print("\n--- Your Tasks ---")
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. {task['description']} [{status}]")

def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_description = input("Enter new task description: ")
            tasks[task_number - 1]["description"] = new_description
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Start the application
if __name__ == "__main__":
    main()