import requests


# Логин для получения токена
login_url = 'http://127.0.0.1:8000/api/token'
login_data = {'username': 'alex', 'password': '123'}

login_response = requests.post(login_url, json=login_data)
token = login_response.json().get('access')
print(len(token))
print(token)
url_protected = 'http://127.0.0.1:8000'

headers = {'Authorization': f'Bearer {token}'}

log = requests.get(url_protected, headers=headers)
print(log.json())
