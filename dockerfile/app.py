import requests
r = requests.get('http://172.17.0.2:8080')
print(r.text)
