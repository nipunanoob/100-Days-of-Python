from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, flightdata):
        
        account_sid = os.getenv('TWILIO_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_phone_no = os.getenv('TWILIO_PHONE_NO')
        user_phone_no = os.getenv('USER_PHONE_NO')
        
        price = flightdata.price
        origin_city = flightdata.origin_city
        origin_airport = flightdata.origin_airport
        destination_city = flightdata.destination_city
        destination_airport = flightdata.destination_airport
        out_date = flightdata.out_date
        return_date = flightdata.return_date
        message = f'Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport} from {out_date} to {return_date}'
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body=message,
                     from_=twilio_phone_no,
                     to=user_phone_no
                 )

        print(message.sid)