import os
import requests
from twilio.rest import Client

OpenWeatherURL = 'https://api.openweathermap.org/data/2.5/onecall?'
OpenWeatherAPI = os.environ.get("OW_API_KEY")

Chicago_Latitude = 41.878113
Chicago_Longitude = -87.629799

TwilioSID = os.environ.get("TW_SID")
TwilioAuth = os.environ.get("TW_AUTH_KEY")

parameters = {
    'lat': Chicago_Latitude,
    'lon': Chicago_Longitude,
    'appid': OpenWeatherAPI,
    'exclude': 'current,minutely,daily'
}

client = Client(TwilioSID, TwilioAuth)
request = requests.get(OpenWeatherURL, params=parameters)
request.raise_for_status()

weather = request.json()
hourly = weather['hourly']

will_it_rain = False

for hour in hourly[:12]:
    if hour['weather'][0]['id'] < 700:
        will_it_rain = True
    
if will_it_rain:
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_="",
            to=""
        )
    print(message.status)
