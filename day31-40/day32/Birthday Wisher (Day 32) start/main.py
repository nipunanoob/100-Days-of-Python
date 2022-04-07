import pandas as pd
import random
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

now = datetime.now()
day = now.day
month = now.month
today = (month, day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    letter = random.choice(letters)
    with open(f"letter_templates/{letter}", 'r') as file:
        data = file.read()
    data = data.replace('[NAME]', birthday_dict[today]['name'].capitalize())
    print(data)
    load_dotenv()
    my_email = os.getenv('MY_EMAIL')
    password = os.getenv("PASSWORD")

    with smtplib.SMTP(os.getenv("SMTP"), os.getenv("PORT")) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs=os.getenv("TARGET_EMAIL"),
            msg=f"Subject: Happy birthday {birthday_dict[today]['name'].capitalize()}\n\n{data}"
        )
else:
    print("Nobody has birthday today..")








