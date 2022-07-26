import requests

sheety_endpoint = "https://api.sheety.co/ed67445fe0c5dc9a234b431dd06130b3/flightDeals/prices/"

class DataManager:
    def __init__(self):
        self.sheet_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint).json()
        self.sheet_data = response['prices']
        # self.sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 58, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 130, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]
        return self.sheet_data
    
    def update_destination_data(self):
        for row in self.sheet_data:
            row_id = row['id']
            new_data = {
                "price": {
                    'iataCode': row['iataCode']
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{row_id}", json=new_data)
            print(response.text)

    