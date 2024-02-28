import csv
import requests
import sys

def fetch_user_tasks(user_id):
    # Fetching tasks for the specified user
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    tasks = response.json()
    return tasks

def export_to_csv(user_id, tasks):
    # Writing tasks to a CSV file
    filename = f'{user_id}.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([user_id, task['userId'], task['completed'], task['title']])

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
    export_to_csv(user_id, tasks)
    print(f"Tasks for user {user_id} exported to {user_id}.csv")

if __name__ == "__main__":
    main()
