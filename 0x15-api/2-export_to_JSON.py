#!/usr/bin/python3
""" For a given employee ID, returns information
about his/her TODO list progress and exports it to a JSON file.
"""

import requests
import json


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
    completed_tasks = [{"task": todo['title'], "completed": todo['completed'],
                        "username": employee_name} for todo in todos_data]

    return {str(employee_id): completed_tasks}


def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    todo_data = get_employee_todo_progress(employee_id)
    filename = f"{employee_id}.json"
    export_to_json(todo_data, filename)
    print(f"Data exported to {filename}")
