#!/usr/bin/python3


def get_weather_api_response():
	import json
	import requests
	try:
		responce_json = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Hrodna&appid=b6627e1c2f78708e4c3b1abed614bfcd')
		if responce_json:
			json_format = responce_json.json()
			return json_format
	except:
		print("Link is invalid")


def get_city_weather(json_format):
	city = str("city: " + json_format['name'])
	temperature_kelvin = int(json_format['main']['temp'])
	temperature_celsiy = ("temperature: " + str(temperature_kelvin - 273) + "C")
	weather = ("weather: " + json_format['weather'][0]['main'])
	humidity = ("humidity: " + str(json_format['main']['humidity']) + "%")
	return city, temperature_celsiy, weather, humidity;

json_format = get_weather_api_response()
if json_format is None:
	print("Request is BAD. Aborting...")
else:
	result = get_city_weather(json_format)
	print(f'{result[0]}', '\n' f'{result[1]}', '\n' f'{result[2]}', '\n' f'{result[3]}')
