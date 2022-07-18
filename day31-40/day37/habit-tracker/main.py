import requests
from datetime  import date,timedelta
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv('PIXELA_TOKEN')
USERNAME = os.getenv('PIXELA_USERNAME')
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
pixela_graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": 'Sleeping graph',
    "unit": "Hours",
    'type': "float",
    "color": "ajisai"
}
request_headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=pixela_graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# today = date.today()
# yesterday = (today - timedelta(1)).strftime("%Y%m%d")

today = date.today().strftime("%Y%m%d")



selected_graph_endpoint = f"{pixela_graph_endpoint}/{graph_id}"
selected_graph_add_pixel_config = {
    'date': today,
    'quantity': input("How mnay hours did you sleep yesterday?")
}

#Creates pixel
response = requests.post(url=selected_graph_endpoint, json=selected_graph_add_pixel_config, headers=request_headers)
print(response.text)

# selected_graph_update_pixel_config = {
#     'quantity': "6"
# }

#Updates pixel
# print(f"{selected_graph_endpoint}/{today}")
# response = requests.put(url = f"{selected_graph_endpoint}/{today}",json= selected_graph_update_pixel_config,
#                                     headers=request_headers)

# print(response.text)

#Deletes pixel
# response = requests.delete(url=f"{selected_graph_endpoint}/{yesterday}", headers=request_headers)
# print(response.text)


