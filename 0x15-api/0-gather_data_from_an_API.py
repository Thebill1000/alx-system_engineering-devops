#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests

def get_employee_todo_progress(employee_id):
    # Send a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos = response.json()

        # Get the employee's name
        employee_name = todos[0]['name'].split()[0]

        # Count the number of completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_number_of_tasks = len(todos)

        # Display the progress information
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print("\t", task['title'])
    else:
        print(f"Error: Unable to retrieve TODO list for employee {employee_id}.")

# Prompt the user to enter an employee ID
employee_id = int(input("Enter the employee ID: "))

# Call the function to get the employee's TODO list progress
get_employee_todo_progress(employee_id)
