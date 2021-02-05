
def get_weather_api():
	import json
	import requests
	request_to_API = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Hrodna&appid=b6627e1c2f78708e4c3b1abed614bfcd')
	convert_to_json = request_to_API.json()
	return convert_to_json


def get_city_weather(convert_to_json):
	print("city: " + convert_to_json['name'])
	print("temperature: " + str(int(convert_to_json['main']['temp'] - 273)) + "C")
	print("weather: " + convert_to_json['weather'][0]['main'])
	print("humidity: " + str(convert_to_json['main']['humidity']) + "%")


api = get_weather_api()

show_weather = get_city_weather(api)
