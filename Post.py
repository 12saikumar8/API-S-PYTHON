import requests
api_url="https://jsonplaceholder.typicode.com/todos"
#  todo below is just a name assingment you can use anything
todo={"userid":1,"title":"Sriman","completed":False}
response=requests.post(api_url,json=todo)  
print(response.json())

print(response.status_code)


# If you don’t use the json keyword argument to supply the JSON data, 
# then you need to set Content-Type accordingly and serialize the JSON manually.
# Here's eqivalent code of above
import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json())


response.status_code

