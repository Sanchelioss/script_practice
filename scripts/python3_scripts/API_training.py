#!/usr/bin/python3

from requests import get


def get_weather_api_response(link):

	try:
		api_responce = get(link)
		if api_responce:
			responce_json = api_responce.json()
			return responce_json
	except:
		return None


def get_city_weather(responce_json):
	city = str("city: " + responce_json['name'])
	temperature_kelvin = int(responce_json['main']['temp'])
	temperature_celsiy = ("temperature: " + str(temperature_kelvin - 273) + "C")
	weather = ("weather: " + responce_json['weather'][0]['main'])
	humidity = ("humidity: " + str(responce_json['main']['humidity']) + "%")

	return city, temperature_celsiy, weather, humidity;


link = 'http://api.openweathermap.org/data/2.5/weather?q=Hrodna&appid=b6627e1c2f78708e4c3b1abed614bfcd'
responce_json = get_weather_api_response(link)


if responce_json is None:
	print("Request is BAD. Aborting...")
else:
	result = get_city_weather(responce_json)
	print(f'{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}')
