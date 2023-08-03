#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "HEL"
TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
SIX_MONTHS_FROM_TODAY = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

# Create DataManager class and FlightSearch Class
data_manage = DataManager()
flight_search = FlightSearch()
sheet_data = data_manage.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
    data_manage.update_destination_code()

for city in data_manage.destination_data:
    flight_search.flight_check(origin_city_code=ORIGIN_CITY_CODE, destination_city_code=city["iataCode"], from_time=TOMORROW, to_time=SIX_MONTHS_FROM_TODAY)
# pprint(data_manage.destination_data)