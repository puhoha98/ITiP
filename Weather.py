import requests

#ключ openweather
key = '5bdbeab1cde794d80c259051987cacbf'

# получить "красивый" словарь
def getDict (data):
    if data.get('list') is None:
        weather_info = dict(
            s_city=data['name'],
            desc=data['weather'][0]['description'],
            main=data['weather'][0]['main'],
            temp=round(data['main']['temp']),
            maxTemp=round(data['main']['temp_min']),
            minTemp=round(data['main']['temp_max']),
            windSpeed=round(data["wind"]["speed"]),
            humidity=data['main']['humidity'],
            pressure=data['main']['pressure'],
            visibility=data['visibility'],
            date=data['dt']/60/60/24
        )
    else:
        weather_info = {}
        for d in data['list']:
            if "12:00:00" in d['dt_txt']:
                weather_info[d['dt_txt']] = dict(
                    s_city=data['city']['name'],
                    desc=d['weather'][0]['description'],
                    main=d['weather'][0]['main'],
                    temp=round(d['main']['temp']),
                    maxTemp=round(d['main']['temp_min']),
                    minTemp=round(d['main']['temp_max']),
                    windSpeed=round(d["wind"]["speed"]),
                    humidity=d['main']['humidity'],
                    pressure=d['main']['pressure'],
                    visibility=d['visibility'],
                    date=d['dt_txt'],
                )
            if len(weather_info.keys()) == 7:
                break

    return weather_info

# получить погоду на день
def getWeatherDay():
    try:
        weather = getDict(requests.get('http://api.openweathermap.org/data/2.5/weather',
                            params={'APPID': key, 'q': city, 'units': 'metric', 'lang': 'en'}).json())
        # Полученные данные добавляем в текстовую надпись для отображения пользователю
        weatherLabel['text'] = f"{weather['s_city']} weather information."
        weatherLabel['text'] = f"In {weather['s_city']} {weather['desc']} today\n" \
                               f"Temperature {weather['temp']} °C\n" \
                               f"Wind speed {weather['windSpeed']} m/s\n" \
                               f"Max. temp {weather['maxTemp']} °C\n" \
                               f"Min. temp {weather['minTemp']} °C\n" \
                               f"Humidity {weather['humidity']} g/m\n" \
                               f"Visibility {weather['visibility']} m"
    except:
        weatherLabel['text'] = "Weather not found"

# получить погоду на неделю
def getWeatherWeek():
    try:
        weather = getDict(requests.get('http://api.openweathermap.org/data/2.5/forecast',
                                       params={'APPID': key, 'q': city, 'units': 'metric', 'lang': 'en'}).json())
        weatherLabel['text'] = ""

        for i in weather.keys():
            weatherLabel['text'] += f"{weather[i]['date'][:10]}:                      \n" \
                                    f"{weather[i]['main']}, {weather[i]['temp']} °C\n" \
                                    f"{weather[i]['windSpeed']} m/s, {weather[i]['visibility']} m\n\n"
    except:
        weatherLabel['text'] = "Weather not found"

weatherLabel= {
    'text':'',
}

city = input("Введите город")
getWeatherDay()
print(f"Погода на день: {weatherLabel['text']}")

getWeatherWeek()
print(f"Погода на неделю: {weatherLabel['text']}")
