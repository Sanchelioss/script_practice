
def get_weather_api_responce():
	import json
	import requests
	api_responce = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Hrodna&appid=b6627e1c2f78708e4c3b1abed614bfcd')
	json_format = api_responce.json()
	return json_format


def get_city_weather(json_format):
	city = str("city: " + json_format['name'])
	temperature = ("temperature: " + str(int(json_format['main']['temp'] - 273)) + "C")
	weather = ("weather: " + json_format['weather'][0]['main'])
	humidity = ("humidity: " + str(json_format['main']['humidity']) + "%")
	return city, temperature, weather, humidity;

json_format = get_weather_api_responce()

result = get_city_weather(json_format)

print(f'{result[0]}', '\n' f'{result[1]}', '\n' f'{result[2]}', '\n' f'{result[3]}')