#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress and
exports it to a CSV file.
"""

import requests
import csv
import sys


def get_employee_todo_progress_and_export(employee_id):
    # Get user information
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    user_name = user_data.get('name')

    # Get user's TODO list
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODO list for user ID {employee_id}.")
        return

    todos = todos_response.json()

    # Prepare data for CSV export without headers
    data_for_csv = [
        [str(employee_id),
        user_name,
        str(todo['completed']),
        todo['title']] for todo in todos
                    ]

    # Export data to CSV without headers
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data_for_csv[1:]:
            writer.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)
