#!/usr/bin/python3
""" Export data in the json format """
import json
from requests import get
from sys import argv

response = get('https://jsonplaceholder.typicode.com/todos/')
data = response.json()

row = []
response2 = get('https://jsonplaceholder.typicode.com/users')
data2 = response2.json()

for i in data2:
    if i['id'] == int(argv[1]):
        employee = i['username']

    # Define filtered_tasks as an empty list
    filtered_tasks = []
if employee is not None:    
    # Create a dictionary to hold the employee's tasks
    employee_tasks = {
        "employee_id": int(argv[1]),
        "employee_username": employee,
        "tasks": filtered_tasks
    }

    # Export the data to a JSON file
    json_filename = f"{argv[1]}.json"
    with open(json_filename, 'w') as file:
        json.dump(employee_tasks, file, indent=4)
