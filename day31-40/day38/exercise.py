from email import header
from urllib import response
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ID= os.getenv('API_ID')
API_KEY= os.getenv('API_KEY')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

parameters = {
    "query": input("Tell me what exercises you did today?")
}

response = requests.post(url = exercise_endpoint,
                        headers=headers,
                        data=parameters)
result = response.json()
print(result)

#{'exercises': [{'tag_id': 215, 'user_input': 'cricket', 'duration_min': 120, 'met': 4.8,
# 'nf_calories': 672, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/215_highres.jpg', 
# 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/215_thumb.jpg', 'is_user_uploaded': False}, 
# 'compendium_code': 15150, 
# 'name': 'cricket', 'description': None, 'benefits': None}]}

from datetime import datetime, date

today = date.today().strftime("%d/%m/%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

exercise_details = result['exercises'][0]

sheety_endpoint = "https://api.sheety.co/ed67445fe0c5dc9a234b431dd06130b3/workoutTracker/workouts"
sheety_parameters = {
    "workout": {
        "date": today,
        "time": current_time,
        "exercise": exercise_details['name'].title(),
        "duration": exercise_details['duration_min'],
        "calories": exercise_details['nf_calories']
    }
}

sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic bmlwdW46Zmx5aW5ncGVuZ3Vpbjg3'
}


response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers = sheety_headers)
print(response.text)



