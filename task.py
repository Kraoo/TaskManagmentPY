import pickle
import os
import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Due: {self.due_date}, Completed: {self.completed}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, task, new_task):
        index = self.tasks.index(task)
        self.tasks[index] = new_task

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_as_completed(self, task):
        task.completed = True

    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)

def print_menu():
    print("Task Management System")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. List Tasks")
    print("5. Mark Task as Completed")
    print("6. Save Tasks")
    print("7. Load Tasks")
    print("8. Exit")

def get_user_input():
    choice = input("Enter your choice: ")
    return int(choice) if choice.isdigit() else -1

def main():
    task_manager = TaskManager()
    filename = "tasks.pkl"

    while True:
        print_menu()
        choice = get_user_input()

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            task = Task(title, description, due_date, priority)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif choice == 2:
            task_manager.list_tasks()
            if task_manager.tasks:
                index = int(input("Enter index of task to remove: "))
                if 0 <= index < len(task_manager.tasks):
                    task_manager.remove_task(task_manager.tasks[index])
                    print("Task removed successfully.")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to remove.")

        elif choice == 3:
            task_manager.list_tasks()
            if task_manager.tasks:
                index = int(input("Enter index of task to update: "))
                if 0 <= index < len(task_manager.tasks):
                    title = input("Enter new task title: ")
                    description = input("Enter new task description: ")
                    due_date = input("Enter new due date (YYYY-MM-DD): ")
                    priority = input("Enter new priority (High, Medium, Low): ")
                    new_task = Task(title, description, due_date, priority)
                    task_manager.update_task(task_manager.tasks[index], new_task)
                    print("Task updated successfully.")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to update.")

        elif choice == 4:
            task_manager.list_tasks()

        elif choice == 5:
            task_manager.list_tasks()
            if task_manager.tasks:
                index = int(input("Enter index of task to mark as completed: "))
                if 0 <= index < len(task_manager.tasks):
                    task_manager.mark_task_as_completed(task_manager.tasks[index])
                    print("Task marked as completed.")
                else:
                    print("Invalid index.")
            else:
                print("No tasks to mark as completed.")

        elif choice == 6:
            task_manager.save_tasks(filename)
            print("Tasks saved successfully.")

        elif choice == 7:
            task_manager.load_tasks(filename)
            print("Tasks loaded successfully.")

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
