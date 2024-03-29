#!/usr/bin/python3
"""
 a Python script that, using this REST API,- export data in
json format."""

if __name__ == "__main__":
    from sys import argv
    import requests
    import json

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('username')

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todo).json()
    value = [{'task': todo.get('title'), 'completed': todo.get('completed'),
              'username': employee} for todo in todos]
    data = {argv[1]: value}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(data, f)
