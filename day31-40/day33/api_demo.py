import requests
from datetime import datetime

MY_LAT = 9.931233
MY_LONG = 76.267303
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# longitude = response.json()["iss_position"]['longitude']
# latitude = response.json()["iss_position"]['latitude']
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = float(data['results']['sunrise'].split("T")[1].split(":")[0])  # Gets hour of sunrise
sunset = float(data['results']['sunset'].split("T")[1].split(":")[0]) # Gets hour of sunset

time_now_in_hours = datetime.now().hour  # Gets current hour
print(sunrise)
print(sunset)
print(time_now_in_hours)
