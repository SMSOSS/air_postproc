import requests
import configparser
import json

def check_weather():
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['weather']['key']
    url = f"https://api.openweathermap.org/data/2.5/weather?id=1819729&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)
    #print(type(data))
    return data.get('weather')[0].get('main')