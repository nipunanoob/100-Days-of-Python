import time

import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

MY_LAT = 10.006170  # Your latitude
MY_LONG = 76.366501  # Your longitude


while True:
    print("Running ISS overhead notifier script ...")
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

    load_dotenv()
    my_email = os.getenv('MY_EMAIL')
    password = os.getenv("PASSWORD")

    iss_near_current_pos = abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5
    is_sky_dark = sunset <= time_now.hour <= sunrise

    if iss_near_current_pos and is_sky_dark:
        with smtplib.SMTP(os.getenv("SMTP"), os.getenv("PORT")) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("TARGET_EMAIL"),
                msg=f"Subject: Look up in the sky\n\n The ISS is above you in the sky"
            )

    time.sleep(60)
