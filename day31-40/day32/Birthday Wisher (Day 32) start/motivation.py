from datetime import datetime
from random import choice
import os
from dotenv import load_dotenv
import smtplib

# date_of_birth = datetime(year=1999, month=5, day=13)

with open('quotes.txt', 'r') as datafile:
    quotes = datafile.readlines()

quote = choice(quotes)

now = datetime.now()

day_of_week = now.weekday()

if day_of_week == 0:

    load_dotenv()

    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")

    with smtplib.SMTP(os.getenv("SMTP"), os.getenv("PORT")) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.getenv("TARGET_EMAIL"),
            msg=f"Subject:Demo motivational quote\n\n{quote}"
        )
else:
    print("Today is not a Monday")


