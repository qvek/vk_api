import requests
import weather

token = 'trnsl.1.1.20181028T153716Z.945fd59b26ff30f1.8511d1a6e1de1600ae516728870064494d85626e'

def translate_weather():

    text = weather.get_weather()
    request = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',
                       params={'key':token,
                               'text':[text['weather'],
                                text['description']],
                               'lang':'en-ru'}).json()

    weather_now = request['text']
    weather_now.append(text['temperature'])
    print(weather_now)
    print(type(weather_now))
    return weather_now

def translate_weather_now():
    text = weather.weather_now()
    request = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',
                       params={'key':token,
                               'text':text['temp_now'],
                               'lang':'en-ru'}).json()
    weather_now = request['text']
    return weather_now

