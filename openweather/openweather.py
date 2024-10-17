import requests
api_key = open("open_weatherapikey.txt", "r").read()

user_location = input("Please enter your location: ").title()

result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_location}&units=metric&APPID={api_key}")
print(result)

