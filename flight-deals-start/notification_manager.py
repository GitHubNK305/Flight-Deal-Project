from twilio.rest import Client

ACCOUNT_SID = "AC4359b26b93c3ea67351a7c33d0184a81"
AUTH_TOKEN = "fb4819bf7d25d3eb31274b0fc38d4a9f"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sent_notification(self, price, departure_city_name, departure_airport_iata, arrival_city_name,
                          arrival_airport_iata, outbound_data, inbound_date):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body=f"Low price alert! Only €{price} to flight from"
                 f" {departure_city_name}-{departure_airport_iata}"
                 f" to {arrival_city_name}-{arrival_airport_iata}, "
                 f"from {outbound_data} to {inbound_date}.",
            from_='+19382014061',
            to='+358509184234'
        )

        print(message.status)