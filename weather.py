import requests

token = 'f10667083c9444d00ee81ab4bc7bb901'
def get_weather():
    request = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                       params={'id':524901,'APPID':token}).json()

    temperature = {
               'minimum':request['list'][0]['main']['temp_min']-273.15,
               'maximum':request['list'][0]['main']['temp_max']-273.15}

    weather = {'weather':request['list'][0]['weather'][0]['main'],
           'description':request['list'][0]['weather'][0]['description'],
               # 'temperature':round(temperature['avg'], 2)
               }

    return weather

def weather_now():
    request = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                           params={'id': 524901, 'APPID': token}).json()

    weather = {
        'temp_now':round(request['list'][0]['main']['temp']-273.15, 2),
    }
    return weather
