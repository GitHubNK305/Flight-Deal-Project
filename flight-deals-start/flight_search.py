import requests

LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
LOCATION_API_KEY = "DbITEzJi1mV-aVk9f90qDGX4NsZfVvwR"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):

        header = {
            "apikey": LOCATION_API_KEY
        }

        parameter = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=LOCATION_ENDPOINT, headers=header, params=parameter)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

        # code = "TESTING"
        # return code
