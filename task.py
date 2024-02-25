import json
import datetime

class Task:
    def __init__(self, title, description, due_date, status='Pending'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"Task(title='{self.title}', description='{self.description}', due_date='{self.due_date}', status='{self.status}')"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def update_task_status(self, task, status):
        task.status = status

    def get_all_tasks(self):
        return self.tasks

def save_tasks_to_file(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks_from_file(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            tasks = [Task(task['title'], task['description'], task['due_date'], task['status']) for task in data]
            return tasks
    except FileNotFoundError:
        return []

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks_from_file()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task Status")
        print("4. View All Tasks")
        print("5. Save Tasks to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            print("Select a task to delete:")
            for i, task in enumerate(task_manager.get_all_tasks(), start=1):
                print(f"{i}. {task.title}")
            index = int(input("Enter task number: ")) - 1
            task_manager.delete_task(task_manager.get_all_tasks()[index])
            print("Task deleted successfully.")

        elif choice == '3':
            print("Select a task to update status:")
            for i, task in enumerate(task_manager.get_all_tasks(), start=1):
                print(f"{i}. {task.title} - {task.status}")
            index = int(input("Enter task number: ")) - 1
            new_status = input("Enter new status: ")
            task_manager.update_task_status(task_manager.get_all_tasks()[index], new_status)
            print("Task status updated successfully.")

        elif choice == '4':
            print("\nAll Tasks:")
            for i, task in enumerate(task_manager.get_all_tasks(), start=1):
                print(f"{i}. {task.title} - {task.description} - Due: {task.due_date} - Status: {task.status}")

        elif choice == '5':
            save_tasks_to_file(task_manager.get_all_tasks())
            print("Tasks saved to file successfully.")

        elif choice == '6':
            print("Exiting...")
            save_tasks_to_file(task_manager.get_all_tasks())
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
