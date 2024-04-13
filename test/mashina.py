import requests

key = 'ar355ajjgkz5pxxv5g3dfakx'
url = f'https://api.edmunds.com/api/editorial/v3/makes/{mercedez-benz}/models/{a-class}/years/{amg-gt}/expertcontent?api_key={key}'


response = requests.get(url)
print(response.json())