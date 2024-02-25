# Task Management System

This Python program is a simple task management system that allows users to perform various operations on tasks such as adding, deleting, updating status, viewing all tasks, and saving tasks to a file. It utilizes object-oriented programming principles and file I/O for data storage.

## Components

### Task Class
- The `Task` class represents individual tasks with attributes such as title, description, due date, and status.
- It includes an `__init__` method for initializing task attributes and a `__repr__` method for providing a string representation of the task object.

### TaskManager Class
- The `TaskManager` class manages a collection of tasks.
- It includes methods for adding, deleting, and updating task status, as well as retrieving all tasks.

### File Handling Functions
- `save_tasks_to_file`: Writes tasks to a JSON file.
- `load_tasks_from_file`: Reads tasks from a JSON file.

### Main Function
- The `main` function serves as the entry point for the program.
- It presents a menu-driven interface for users to interact with the task management system.

## Usage

1. **Adding a Task**: Users can add a new task by providing a title, description, and due date.

2. **Deleting a Task**: Users can select a task from the list and delete it.

3. **Updating Task Status**: Users can update the status of a task by selecting it from the list and providing a new status.

4. **Viewing All Tasks**: Users can view all existing tasks along with their details such as title, description, due date, and status.

5. **Saving Tasks to File**: Users can save all tasks to a JSON file.

6. **Exiting**: Users can exit the program, which also saves tasks to the file before exiting.

## File Structure

- `task_management.py`: Python script containing the implementation of the task management system.
- `tasks.json`: JSON file used for storing tasks data.

## Running the Program

1. Ensure you have Python installed on your system.
2. Run the `task_management.py` script using a Python interpreter.
3. Follow the on-screen prompts to interact with the task management system.

## Dependencies

- This program relies on Python's built-in libraries such as `json` and `datetime`. No external dependencies are required.