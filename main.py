import requests
from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

parameters = {
    "lat": os.environ["LAT"],
    "lon": os.environ["LON"],
    "appid": os.environ["OMW_API_KEY"],
    'cnt': 4,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()

for hour_data in data['list']:
    if hour_data['weather'][0]['id'] < 700:
        message = client.messages.create(
            body='Będzie padało w ciągu następnych 12 godzin!!!',
            from_=os.environ["TWILIO_NUM"],
            to=os.environ["MY_NUMBER"],
        )
        print(message.status)
        break
print('Kod wykonany poprawnie.')
