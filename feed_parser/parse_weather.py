import json
import requests


def get_weather(query):
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    weather_key = '&appid=b3def1391fcf07b02527845578229679'
    city = query
    req_url = weather_url + city + weather_key
    # data = requests.get(req_url).text
    # read_data = json.loads(data)
    # print(read_data)
    data = requests.get(req_url)
    read_data = data.json()
    if read_data.get('weather'):
        weather = {"description": read_data['weather'][0]['description'],
                   "temperature": read_data['main']['temp'],
                   "city": read_data['name'],
                   "icon": read_data['weather'][0]['icon']
                   }
    return weather
