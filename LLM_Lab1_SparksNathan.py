# Nathan Sparks
# 19 April 2026
# LLM_LAB1
# Using AI to generate python script

import os
from datetime import datetime

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    tasks = []
    if not os.path.exists(FILENAME):
        return tasks

    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                task, date, completed = parts
                tasks.append({
                    "task": task,
                    "date": date,
                    "completed": completed == "True"
                })
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']} | {t['date']} | {t['completed']}\n")

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nTo-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["completed"] else "✘"
        print(f"{i}. [{status}] {t['task']} (Added: {t['date']})")
    print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({
            "task": task,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "completed": False
        })
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task cannot be empty.\n")

def remove_task(tasks):
    """Remove a task."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Removed: {removed['task']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Enter a valid number.\n")

def mark_completed(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()