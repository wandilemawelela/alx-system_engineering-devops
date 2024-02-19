#!/usr/bin/python3
""" For a given employee ID, returns information
about his/her TODO list progress.
"""

import requests


def get_employee_todo_progress(employee_id):
    # Fetch user info
    user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's todos
    todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Count completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Print progress
    print(f"Employee {employee_name} is done with tasks"
          f"({num_completed_tasks}/{total_tasks}):")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
