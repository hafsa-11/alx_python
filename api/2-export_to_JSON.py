import json
import requests
import sys

def fetch_user_tasks(user_id):
    # Fetching tasks for the specified user
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks = response.json()
    return tasks

def export_to_json(user_id, tasks):
    # Creating JSON object
    data = {str(user_id): []}
    for task in tasks:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": task['username']  # Assuming username is provided in the task data
        }
        data[str(user_id)].append(task_data)

    # Writing JSON object to a file
    filename = f'{user_id}.json'
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    try:
        user_id = int(user_id)
    except ValueError:
        print("Error: USER_ID must be an integer.")
        sys.exit(1)

    tasks = fetch_user_tasks(user_id)
    export_to_json(user_id, tasks)
    print(f"Tasks for user {user_id} exported to {user_id}.json")

if __name__ == "__main__":
    main()
