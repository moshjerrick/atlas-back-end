#!/bin/bash/python3


import requests
import sys

def get_employee_todo_progress(employee_id):
    # Get user information
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    user_name = user_data.get('name')

    # Get user's TODO list
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODO list for user ID {employee_id}.")
        return

    todos = todos_response.json()

    # Calculate progress
    total_todos = len(todos)
    completed_todos = [todo for todo in todos if todo['completed']]
    number_of_completed_todos = len(completed_todos)

    # Display progress
    print(f"Employee {user_name} is done with tasks({number_of_completed_todos}/{total_todos}):")
    for todo in completed_todos:
        print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
