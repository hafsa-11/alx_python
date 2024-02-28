"""
Export User Tasks to JSON

This script fetches tasks owned by users from an API and exports them to a JSON file.
The exported JSON file contains task details such as task title, completion status, and username.

Usage:
    python3 script_name.py

Example:
    python3 script_name.py
"""

import json
import requests

def fetch_user_tasks(user_id):
    """
    Fetch tasks for the specified user from an API.

    Args:
        user_id (int): The ID of the user whose tasks are to be fetched.

    Returns:
        list: A list of tasks owned by the specified user.
    """
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks = response.json()
    return tasks

def export_to_json():
    """
    Export tasks of all employees to a JSON file.
    """
    all_tasks = {}
    for user_id in range(1, 11):  # Assuming there are 10 users
        tasks = fetch_user_tasks(user_id)
        all_tasks[str(user_id)] = [{"username": task['username'], "task": task['title'], "completed": task['completed']} for task in tasks]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f, indent=4)

def main():
    """
    Main function to export tasks of all employees to a JSON file.
    """
    export_to_json()
    print("Tasks for all employees exported to todo_all_employees.json")

if __name__ == "__main__":
    main()
