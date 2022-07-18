import requests
from twilio.rest import Client
import config

api_key = config.OWM_api_key
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

#  ARIZONA LAT & LONG
# MY_LAT = 34.048927
# MY_LONG = -111.093735

#  Cochin LAT & LONG
MY_LAT = 9.957620
MY_LONG = 76.251152

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data['hourly'][0:12]

will_rain = False
for hour_data in hourly_weather_data:
    if hour_data['weather'][0]['id'] < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today, please bring an ☔",
        from_=config.twilio_phone_num,
        to=config.my_phone_num
    )
    print(message.status)
