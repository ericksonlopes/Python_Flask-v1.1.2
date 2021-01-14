import requests

# 07
get = requests.post('http://127.0.0.1:5000/login')

print(get.text)

#