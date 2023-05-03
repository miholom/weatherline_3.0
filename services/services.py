import requests

def location_city():
    # get gps coordinates from geopy
    import json

    # import urlopen from urllib.request
    from urllib.request import urlopen

    # open following url to get ipaddress
    urlopen("http://ipinfo.io/json")

    # load data into array
    data = json.load(urlopen("http://ipinfo.io/json"))

    # extract city
    city = data['city']

    return city




def weather():
    city = location_city()
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
            'q': city, 
            'appid': '111e9ebf80f660a29dad97db9394d294',
            'units': 'metric',
            'lang': 'ru',
            }
    res = requests.get(api_url, params=params)
    data = res.json()

    vis_print: str
    VISIBILITY: dict()

    VISIBILITY = { 
                "SMALL": "дымка, ебучие заводы",
                "MIDDLE": "нормальная, жить можно",
                "HIGH": "отличная, походу был ветер",
                }
    
    if data['visibility'] <= 1000:
        vis_print = VISIBILITY["SMALL"]
    elif  1000 < data['visibility'] <= 6000:
        vis_print = VISIBILITY["MIDDLE"]
    elif 6000 < data['visibility'] <= 10000:
        vis_print = VISIBILITY["HIGH"]

    template = 'aктуальная температура в {}e является {} градуса Цельсия, скорость ветра {} м/с, {}. Видимость - {}.'
    temp = template.format (data['name'], data['main']['temp'], data['wind']['speed'], data['weather'][0]['description'], vis_print)
    
    return temp