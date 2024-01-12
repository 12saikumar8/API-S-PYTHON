#  below code is to see the existing data
# Here, you first call requests.get() to view the contents of the existing todo. below 10 at end is id where to update data
import requests
api_url="https://jsonplaceholder.typicode.com/todos/10"
response=requests.get(api_url)
print(response.json())

# Next, you call requests.put() with new JSON data to replace the existing to-do’s values.
# here we are updating data in place of id :10
todo={"userId":1,"title":"Goodboy", "Completed":False}

response=requests.put(api_url,json=todo)
print(response.json())

print(response.status_code)

