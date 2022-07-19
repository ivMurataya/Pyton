STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "DOJMK9ZTQEAPEYYR"
NEW_API_KEY = "68b72601843743f8823c166eb29f4116"

import requests
import datetime as dt
import smtplib
import html

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
now = dt.datetime.now().date()
yesterday = now - dt.timedelta(days=1)
y = str(yesterday)
n = str(now)
stockDiff = 0.0


def percentageDiff():
    global stockDiff
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": "DOJMK9ZTQEAPEYYR"
    }
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=parameters)
    v2Now = float(r.json()["Time Series (Daily)"][n]["1. open"])
    v1Yesterday = float(r.json()["Time Series (Daily)"][y]["4. close"])
    print(f"Today {v2Now}  Yesteday {v1Yesterday}")
    # Percentage change change from V1 to V2
    diff = ((v2Now - v1Yesterday) / v1Yesterday) * 100
    stockDiff = diff
    print(round(stockDiff,3))
    return diff


def getNews():
    parameters = {
        "q": "Tesla Inc",
        "from": n,
        "sortBy": "popularity",
        "apiKey": NEW_API_KEY

    }
    url = "https://newsapi.org/v2/everything"
    r = requests.get(url, params=parameters)
    data = r.json()["articles"]
    newEmail()
    try:
        for article in range(0, 3):
            header = str(data[article]["title"])
            desc = str(data[article]["description"])
            buildMail(header, desc)
            print(article, header, desc)
    except IndexError:
        print("Not enough data")


def newEmail():
    icon = ""
    dif = round(stockDiff, 3)
    if stockDiff > 0:
        icon = "+"
    else:
        icon = "-"
    with open("email.txt", mode="w") as file:
        file.write(f"{COMPANY_NAME}: {STOCK} {icon}{abs(dif)} \n")


def buildMail(header,desc):
    with open("email.txt", mode="a") as file:
        file.write(f"{header}\n{desc} \n\n")


def sendEmail():
    my_email = "myemail@gmail.com"
    password = "password"
    with open("email.txt", mode="r") as file:
        content = file.read()
        print(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure connection, encrypts mail
        connection.login(user=my_email, password=password)
        try:
            connection.sendmail(from_addr=my_email, to_addrs="myemail@hotmail.com",
                           msg=f"Subject:Todays news on {COMPANY_NAME}\n\n{content}")
        except:
            print("Contains a (, not valid character. Email not sent")


if abs(percentageDiff()) > 5:
    getNews()
    sendEmail()
    print("Get News")
else:
    print("Stocks under 5%")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
