import requests

filename = "dupa.png"
files = {'file': (filename, open(filename, 'rb'))}
json = {'first': "Hello", 'second': "World"}

response = requests.post(
    'http://127.0.0.1:8000/firebase/post',
    files=files,
)

print(response.json())