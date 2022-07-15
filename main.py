import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
OWN1_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "*************************************"
twilio_account_sid = "**********************************"
twilio_auth_token = "***********************************"


weather_params ={
    "lat":28.636391,
    "lon":76.921349,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWN1_Endpoint,params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain =False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body='Please bring Umbrella ☂ with you today,Beacuse it may rain⛈.',
        from_='**********',
        to='**********'
    )
    print(message.status)