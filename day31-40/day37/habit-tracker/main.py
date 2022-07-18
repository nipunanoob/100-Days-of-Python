from urllib import response
import requests
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv('TOKEN')
user_params = {
    'token': TOKEN,
    'username': 'ginzuka',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

