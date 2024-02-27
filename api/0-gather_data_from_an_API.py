import sys
import requests

def fetch_todo_list(employee_id):
    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch TODO list for the employee
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    # Display employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_list(employee_id)
