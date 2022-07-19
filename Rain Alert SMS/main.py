import requests
import os
from twilio.rest import Client

account_sid = "AC1230048f61c9ca2ef88b4082816290cc"
auth_token = "112aa4fa84646963b3e55740cc44cadd"

url = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
   "lat": "19.772852",
   "lon": "-98.572859",
   "appid": "a3e1cbcd480c47045c09463f2a0f5b9c",
   "units" : "metric",
   "exclude": "daily,minutely"
}
response = requests.get(url=url, params=parameters)
data = response.json()["hourly"]
will_rain = False
for n in range(0,12):
   weather_code = data[n]["weather"][0]["id"]
   weather = data[n]["weather"][0]["main"]
   if int(weather_code) < 700:
      will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                              messaging_service_sid='MGb9c1894a4fe41df5b7168bafd9165e14',
                              body='It is going to rain. Remember to bring an umbrella',
                              to='+527712213449'
                     )

    print(message.status)

