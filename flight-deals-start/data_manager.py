import requests
import os

os.environ["SHEETY_ENDPOINT"] = "https://api.sheety.co/2b8377bb26f8127764d39f3e85ff93a1/flightDeals/prices"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": city
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()
            # print(response.text)
