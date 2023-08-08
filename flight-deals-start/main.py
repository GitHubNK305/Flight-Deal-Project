# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "HEL"
TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
SIX_MONTHS_FROM_TODAY = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")


# Create DataManager class and FlightSearch Class6
data_manage = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manage.get_destination_data()
emails = data_manage.get_customer_emails()
# print(emails)
if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
    data_manage.update_destination_code()


for city in data_manage.destination_data:
    flight_data = flight_search.flight_check(origin_city_code=ORIGIN_CITY_CODE, destination_city_code=city["iataCode"],
                                             from_time=TOMORROW, to_time=SIX_MONTHS_FROM_TODAY)
    if flight_data.price < city["lowestPrice"]:
        message = f"Low price alert! Only Euro {flight_data.price} to flight from {flight_data.origin_city}-{flight_data.origin_airport} to " \
                  f"{flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}."
#        print("You can buy your ticket and plan your trip.")
        if flight_data.stop_overs > 0:
            message = f"Low price alert! Only Euro {flight_data.price} to flight from {flight_data.origin_city}-{flight_data.origin_airport} to " \
                  f"{flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}.\n" \
                      f"Flights has {flight_data.stop_overs} stopovers, via {flight_data.via_city}."
        # notification_manager.sent_notification(message)
        for email in emails:
            # print(email["email"])
            notification_manager.send_emails(email["email"], message)
#pprint(flight_data.price)
