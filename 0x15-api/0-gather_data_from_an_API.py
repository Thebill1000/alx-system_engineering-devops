#!/usr/bin/python3
"""Returns to-do list information for a given employee"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('name')

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todo).json()
    done = [todo for todo in todos if todo.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        employee, len(done), len(todos)))
    for d in done:
        print("\t ", d.get('title'))
