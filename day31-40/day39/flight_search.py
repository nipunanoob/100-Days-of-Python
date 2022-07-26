import requests
from flight_data import FlightData

from dotenv import load_dotenv
import os

load_dotenv()

flight_endpoint = "https://tequila-api.kiwi.com"
API_KEY = os.getenv("FLIGHT_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self):
        
        headers = {
            'apiKey': API_KEY
        }
        parameters = {
            'term': self.cityname
        }
        data = (requests.get(url= f"{flight_endpoint}/locations/query", params=parameters, headers=headers))
        
        response = data.json()
        iatacode = response["locations"][0]["code"]
        return iatacode
    
    def check_flights(self, departure_city_code, arrival_city_code, from_time, to_time):
        parameters = {
            "fly_from": departure_city_code,
            "fly_to": arrival_city_code,
            "date_from":  from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "max_stopovers": 0,
            "flight_type": "round"
        }
        headers = {
            'apiKey': API_KEY
        }
        
        response = requests.get(url=f"{flight_endpoint}/v2/search", params=parameters, headers=headers)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {arrival_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data