import requests

# 07
get = requests.post('http://127.0.0.1:5000/login', data={'username': 'Erickson', 'password': 'Erickson2'})

print(get.text)

#a