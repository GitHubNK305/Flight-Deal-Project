import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = "Your tequila apikey"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        header = {
            "apikey": API_KEY
        }

        parameter = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=parameter)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

        # code = "TESTING"
        # return code

    def flight_check(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            "apikey": API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "one_for_city": 1,
            "curr": "EUR",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)
        response.raise_for_status()
        # print(response.text)

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)
            response.raise_for_status()
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=2,
                via_city=data["route"][0]["cityTo"]
            )
            print(f"{flight_data.destination_city}: Eur {flight_data.price}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{flight_data.destination_city}: Eur {flight_data.price}")
            return flight_data
