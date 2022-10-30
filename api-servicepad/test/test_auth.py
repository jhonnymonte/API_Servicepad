import pytest
import json
import requests

"""
how to run the test

first:
open a system terminal
activates the virtual environment of the project with pipenv shell
and run the server with "python apps.py".
second
open another terminal and place the directory in the test folder of the api-servicepad project.
and then run `pytest -s test_auth.py`.
"""

base_url = "http://127.0.0.1:5000"


user_test_data ={
  "email" : "test@test.com",
  "password": "testPass"
}

session = requests.Session()
session.headers.update([('Content-Type', 'application/json')])


def test_login():
    """
     test function to login for a existing user
    """
    url = base_url + "/api/auth/login"
    data = json.dumps(user_test_data)
    response = session.post(url, data= data)
    print(f"Login response: {response.json()}")
    assert response.status_code == 200