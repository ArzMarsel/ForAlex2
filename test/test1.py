import requests

url = 'http://127.0.0.1:8000/'

# response = requests.get(url)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print('Error', response.status_code)


date = {
    'name': 'Nick',
    'age': '23',
    'date_of_burn': '2024-02-02'
}
response = requests.post(url, data=date)


if response.status_code == 201:
    print(response.json())
else:
    print('Error', response.status_code)