#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
Usage: python3 script.py <employee_id>
"""

import csv
import requests
import sys

def fetch_todo_data(employee_id):
    """
    Fetches TODO list data for a given employee ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of dictionaries representing TODO list data.
    """
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos", params={"userId": employee_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching TODO list data: {err}")
        sys.exit(1)

def export_to_csv(employee_id, todos):
    """
    Exports TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        todos (list): List of dictionaries representing TODO list data.
    """
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        user = fetch_user_data(employee_id)
        username = user.get("username")
        for task in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

def fetch_user_data(employee_id):
    """
    Fetches user data for a given employee ID from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: Dictionary representing user data.
    """
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching user data: {err}")
        sys.exit(1)

if __name__ == "__main__":
    # Check for correct number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line argument and validate it
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)

    todos = fetch_todo_data(employee_id)
    export_to_csv(employee_id, todos)
    print(f"Data exported to {employee_id}.csv successfully.")
