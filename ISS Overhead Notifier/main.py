import time

import requests
import datetime as dt
import smtplib

MY_LAT = 19.8063010
MY_LONG = -98.5060045

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    isslongi = float(data["iss_position"]["longitude"])
    isslati = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= isslati <=MY_LAT+5 and MY_LONG -5 <= isslongi <= MY_LONG+5:
        return True

def is_Night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "date": "today"
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 7
    print(sunrise)
    print(sunset)
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_Night() and is_iss_overhead():
        my_email = "myemail@gmail.com"
        password = "password"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure connection, encrypts mail
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="email@hotmail.com",
                                msg="Subject:Look Up\n\nThe ISS is above you in the sky")
            print("Email Sent")




