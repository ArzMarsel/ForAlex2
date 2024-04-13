import requests

key = 'ctRtJmxBD2iItGJGv8fJvLO7TnWQJmIQ1CaGtAWN'
url = f'https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&api_key={key}'


response = requests.get(url)
print(response.json())