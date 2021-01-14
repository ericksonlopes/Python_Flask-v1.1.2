import requests

# 10
# post = requests.post('http://127.0.0.1:5000/login', data={'username': 'Erickson', 'password': 'Erickson2'})
#
# print(post.text)

# 10

# 11

files = {'file': open('11_text.txt', 'rb')}


files_post = requests.post('http://127.0.0.1:5000/', files=files)

print(files_post.text)

