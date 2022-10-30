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
and then run `pytest -s test_publications.py`.
"""

base_url = "http://127.0.0.1:5000"

publication_test= {
  "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC",
  "priority": "High",
  "status": True,
  "title": "What is Lorem Ipsum?"
}

session = requests.Session()
session.headers.update([('Content-Type', 'application/json')])

@pytest.mark.skip
def test_addbook():
    """
     test function to add publication method
    """
    url = base_url + "/addbook"
    data = json.dumps(publication_test)
    response = session.post(url, data= data)
    print(f"Add publication response: {response.json()}")
    assert response.status_code == 200
