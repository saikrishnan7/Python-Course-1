import json
import config
import bcrypt
import base64

# Function to retrieve users from the JSON file
def users():
    try:
        with open(config.FILE_PATH, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at '{config.FILE_PATH}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{config.FILE_PATH}'")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to add a new user to the JSON file
def add_user(user):
    try:
        data = users()
        if data is None:
            data = []
        data.append(user.__dict__)
        with open(config.FILE_PATH, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to get the stored password decoded from base64 as bytes
def get_stored_password_as_bytes(encoded_hashed_pw):
    return base64.b64decode(encoded_hashed_pw.encode('utf-8'))

# Function to authenticate a user
def authenticate_user(username, password):
    data = users()
    if data is None:
        print('User not found. Please register.')
        return None
    for u in data:
        if u['username'] == username:
            if bcrypt.checkpw(password.encode('utf-8'), get_stored_password_as_bytes(u['password'])):
                print('User authenticated')
                return u
            else:
                print('Invalid password')
                return None
    print('User not found. Please register.')
    return None

# Function to add a new task for a user
def add_task(task, user):
    data = users()
    if data is None:
        print('User not found. Please register.')
        return None
    for u in data:
        if u['username'] == user["username"]:
            u['task_list'][task.id] = task.__dict__
            with open(config.FILE_PATH, 'w') as file:
                json.dump(data, file)
            return task.id
    print('User not found. Please register.')
    return None

# Function to view tasks for a user
def view_tasks(user):
    data = users()
    if data is None:
        print('User not found. Please register.')
        return None
    for u in data:
        if u['username'] == user["username"]:
            return u['task_list']
    return dict()

# Function to mark a task as complete
def mark_task_as_complete(id, user):
    data = users()
    if data is None:
        print('User not found. Please register.')
        return
    for u in data:
        if u['username'] == user["username"]:
            if id in u['task_list']:
                u['task_list'][id]['status'] = 'Completed'
                with open(config.FILE_PATH, 'w') as file:
                    json.dump(data, file)
                print(f'Task with id: {id} was marked as completed successfully.')
                return
            else:
                print(f'Task with id: {id} not found.')
                return
    print(f'Task with id: {id} not found.')

# Function to delete a task
def delete_task(id, user):
    data = users()
    if data is None:
        print('User not found. Please register.')
        return None
    for u in data:
        if u['username'] == user["username"]:
            if id in u['task_list']:
                del u['task_list'][id]
                with open(config.FILE_PATH, 'w') as file:
                    json.dump(data, file)
                print(f'Task with id: {id} was deleted successfully.')
                return
            else:
                print(f'Task with id: {id} not found.')
                return
    print(f'Task with id: {id} not found.')