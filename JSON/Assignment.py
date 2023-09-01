import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

todos = json.loads(response.text)

for task in todos:
    if task['completed'] == True:
        print(task)
