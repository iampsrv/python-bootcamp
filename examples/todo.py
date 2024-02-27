# Initialize the ToDo list as an empty dictionary
# Tasks will be stored with a unique id as the key and a dictionary containing the 'description' and 'due_date' as the value
todo_list = {}

# Function to add a task
def add_task(description, due_date=None):
    task_id = len(todo_list) + 1  # Generate a simple unique ID for the task
    todo_list[task_id] = {'description': description, 'due_date': due_date}
    print(f"Task added with ID: {task_id}")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("No tasks found.")
        return
    for task_id, task_info in todo_list.items():
        print(f"ID: {task_id}, Description: {task_info['description']}, Due Date: {task_info.get('due_date', 'N/A')}")

# Function to update a task
def update_task(task_id, new_description=None, new_due_date=None):
    if task_id in todo_list:
        if new_description:
            todo_list[task_id]['description'] = new_description
        if new_due_date:
            todo_list[task_id]['due_date'] = new_due_date
        print(f"Task {task_id} updated.")
    else:
        print(f"Task with ID {task_id} not found.")

# Function to delete a task
def delete_task(task_id):
    if task_id in todo_list:
        del todo_list[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")

# Demo usage
add_task("Buy groceries")
add_task("Read a book", "2023-01-10")
view_tasks()

update_task(1, new_description="Buy groceries and drinks")
delete_task(2)
view_tasks()
