# todo.py

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file if it exists."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)
    return tasks

def save_tasks(tasks):
    """Write all tasks back to the file."""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks with numbers."""
    if not tasks:
        print("\n✅ Your to-do list is empty.\n")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task to the list."""
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print("✅ Task added.")
    else:
        print("⚠️ Empty task not added.")

def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"✅ Removed task: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("👋 Goodbye! Tasks saved.")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
