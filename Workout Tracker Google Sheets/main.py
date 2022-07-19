import requests
import datetime

APP_ID = "a4589e4a"
API_KEY = "80d499e13d984a36387e61b2f7f59e78"
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

x = datetime.datetime.now()
date = x.strftime("%d/%m/%Y")
time = x.strftime("%X")
print(time)
print(date)
exDone = input("Which Excerxise did you do? ")


def UploadData(exName, duration, cal):
    googleURL = "https://api.sheety.co/0737be90ea4f8eab78a8184f01e0ac00/pytonProject/hoja1"
    dataEx = {
        "hoja1": {
            "date": date,
            "time": time,
            "exercise": exName,
            "duration": duration,
            "calories": cal
        }
    }
    auth = {
        "Authorization": "Bearer asdfghdjsafdsfdsawer543gfd"
    }
    googlePost = requests.post(url=googleURL, json=dataEx, headers=auth)
    print(googlePost.status_code)
    print(googlePost.text)


def getData():
    for n in data["exercises"]:
        exName = n["name"]
        duration = n["duration_min"]
        calories = n["nf_calories"]
        UploadData(exName, duration, calories)


dataInput = {
    "query": exDone,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 180.04,
    "age": 25
}
headres = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

result = requests.post(url=url, json=dataInput, headers=headres)
data = result.json()
getData()
print("Result Code Status ", result.status_code)

# ---------------- GET GOOGLE SHEET ------------------

# googleResult = requests.get(googleURL)
# print(googleResult.status_code)
# print(googleResult.text)
