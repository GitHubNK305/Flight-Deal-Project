#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# Create DataManager class and FlightSearch Class
data_manage = DataManager()
flight_search = FlightSearch()
data_manage.get_destination_data()

for city in data_manage.destination_data:
    city["iataCode"] = flight_search.get_destination_code(city["city"])

data_manage.update_destination_code()
# pprint(data_manage.destination_data)