#!/usr/bin/python3
""" For all employees, returns information about
their TODO list progress and exports it to a JSON file.
"""

import json
import requests


def get_all_employees_todo_progress():
    all_employees_data = {}

    # Fetch data for all employees
    for employee_id in range(1, 11):
        # Fetch user info
        user_response = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch user's todos
        todos_response = requests.get("https://jsonplaceholder.typicode.com"
                                      "/todos?userId=" + str(employee_id))
        todos_data = todos_response.json()

        # Store tasks for this employee
        employee_tasks = []
        for todo in todos_data:
            employee_tasks.append({"username": employee_name,
                                   "task": todo['title'],
                                   "completed": todo['completed']})

        # Record tasks for this employee
        all_employees_data[str(employee_id)] = employee_tasks

    return all_employees_data


def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    all_employees_todo_data = get_all_employees_todo_progress()
    filename = "todo_all_employees.json"
    export_to_json(all_employees_todo_data, filename)
    print(f"Data exported to {filename}")
