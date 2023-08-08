from twilio.rest import Client
import smtplib

ACCOUNT_SID = "XX"
AUTH_TOKEN = "XX"

MY_EMAIL = "jintao.helsinki@gmail.com"
PASSWORD = "XX"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def sent_notification(self, message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body=message,
            from_='+19382014061',
            to='+358509184234'
        )

        print(message.status)

    def send_emails(self, to_email, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=to_email,
                                msg=f"Subject: Low Price Alert! \n\n{message}"
                                )

