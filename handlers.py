import random
import webbrowser
from num2words import num2words
import datetime

import requests
from geopy.geocoders import Nominatim
import pyautogui

from voice import voice


def thanks(text):
    options = [
        'Было несложно!',
        'Вам спасибо',
        'Обращайтесь'
    ]
    voice.text_to_speech(random.choice(options))


def weather(text):
    geolocator = Nominatim(user_agent="Tester")
    location = geolocator.geocode("Санкт-Петербург")
    url = ('http://api.openweathermap.org/data/2.5/weather?'
            'lat=' + str(location.latitude) + '&'
            'lon=' + str(location.longitude) + '&'
             'appid=7cdcfaa69a322e2c77fdf3043de45290&'
             'units=metric&'
             'lang=ru')
    r = requests.get(url).json()
    print("погода в Санкт-Петербурге:" + r['weather'][0]['description'] + ", температура:" + num2words(int(r['main']['temp']), lang='ru') + "по Цельсию" + ", давление:" + num2words(int(r['main']['pressure']), lang='ru') + "гекто-паскаль" + ", влажность:" + num2words(int(r['main']['humidity']), lang='ru') + "процентов")
    voice.text_to_speech("погода в Санкт-Петербурге: " + r['weather'][0]['description'] + ", температура: " + num2words(int(r['main']['temp']), lang='ru') + "градусов по Цельсию" + ", давление: " + num2words(int(r['main']['pressure']), lang='ru') + " гекто-паскаль" + ", влажность: " + num2words(int(r['main']['humidity']), lang='ru') + " процентов")


def time(text):
    voice.text_to_speech("время сейчас: " + num2words(datetime.datetime.now().time().hour, lang='ru') + " часов " + num2words(datetime.datetime.now().time().minute, lang='ru') + " минут и " + num2words(datetime.datetime.now().time().second, lang='ru') + "секунд",)


def future(text):
    options = [
        'Сейчас',
        'Понял',
        'Без проблем'
    ]
    voice.text_to_speech(random.choice(options))
    webbrowser.open('https://yandex.ru/pogoda/saint-petersburg?lat=59.938784&lon=30.314997', new=0, autoraise=True)

def close(text):
    options = [
        'За работу',
        'Хватит на сегодня, да?',
    ]
    pyautogui.hotkey('ctrl', 'w')
    voice.text_to_speech(random.choice(options))
