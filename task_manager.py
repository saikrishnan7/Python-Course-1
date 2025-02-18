import data_operations
import getpass
import pprint
import task
import user

# Check if the username is unique
def is_unique(username):
    for u in data_operations.users():
        if u["username"] == username:
            return False
    return True

# Register a new user
def register_user():
    username = input('Enter a username:')
    while not is_unique(username.casefold()):
        username = input('Username already exists. Please enter a different username:')

    password = getpass.getpass('Enter your password:')
    new_user = user.User(username, password)
    data_operations.add_user(new_user)

# Add a new task for the user
def add_task(user):
    task_name = ''
    while task_name == '':
        task_name = input('Enter the task name, name must not be empty:')
    task_description = ''
    while task_description == '':
        task_description = input('Enter the task description, description must not be empty:')
    new_task = task.Task(task_name, task_description)
    data_operations.add_task(new_task, user)
    return new_task.id

# View tasks for the user
def view_tasks(user):
    return data_operations.view_tasks(user)

# Mark a task as complete
def mark_task_as_complete(user):
    id = input('Enter the task id:')
    return data_operations.mark_task_as_complete(id, user)

# Delete a task
def delete_task(user):
    id = input('Enter the task id:')
    return data_operations.delete_task(id, user)

# Authenticate the user
def authenticate_user():
    username = input('Enter your username:')  
    password = getpass.getpass('Enter your password:')
    return data_operations.authenticate_user(username.casefold(), password)

# Print dictionary in a readable format
def print_dict(my_tasks):
    if len(my_tasks) == 0:
        print('No tasks found.')
    else:
        pprint.pprint(my_tasks)

# Main loop for the task manager
while True:
    print('Welcome to Task Manager. Please choose from the below options:')
    print('1. Register')
    print('2. Log in')
    print('3. Quit')
    user_input = input()
    if user_input == '1':
        register_user()
    elif user_input == '2':
        u = authenticate_user()
        if u is not None:
            while True:
                print('Choose from the below options:')
                print('1. Add Task')
                print('2. View Tasks')
                print('3. Mark Task as Complete')
                print('4. Delete Task')
                print('5. Log out')
                user_input = input()
                match user_input:
                    case '1':
                        task_id = add_task(u)
                        print(f'Task added with ID: {task_id}')
                    case '2':
                        my_tasks = view_tasks(u)
                        print_dict(my_tasks)
                    case '3':
                        mark_task_as_complete(u)
                    case '4':
                        delete_task(u)
                    case '5':
                        break
                    case _:
                        print('Invalid input. Please try again.')
    elif user_input == '3':
        break
    else:
        print('Invalid input. Please try again.')