
def get_weather_api_response():
	import json
	import requests
	api_response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Hrodna&appid=b6627e1c2f78708e4c3b1abed614bfcd')
	if api_response:
		json_format = api_response.json()
		return json_format
	else:
		print("Request is BAD")


def get_city_weather(json_format):
	city = str("city: " + json_format['name'])
	temperature_kelvin = int(json_format['main']['temp'])
	temperature_celsiy = ("temperature: " + str(temperature_kelvin - 273) + "C")
	weather = ("weather: " + json_format['weather'][0]['main'])
	humidity = ("humidity: " + str(json_format['main']['humidity']) + "%")
	return city, temperature_celsiy, weather, humidity;

json_format = get_weather_api_response()
if json_format is None:
	print("STOP")
else:
	result = get_city_weather(json_format)
	print(f'{result[0]}', '\n' f'{result[1]}', '\n' f'{result[2]}', '\n' f'{result[3]}')