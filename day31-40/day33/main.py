import time

import requests
from datetime import datetime

MY_LAT = 10.006170  # Your latitude
MY_LONG = 76.366501  # Your longitude

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    iss_near_current_pos = abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5
    is_sky_dark = sunset <= time_now.hour <= sunrise

    if iss_near_current_pos:
        print("Look up in the sky")
    time.sleep(60)
