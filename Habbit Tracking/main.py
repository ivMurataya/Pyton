import requests
from datetime import datetime
# https://pixe.la/v1/users/ivanm97/graphs/graph1.html
TOKEN = "QAzplm12ds#"
USERNAME = "ivanm97"
endpoint = "https://pixe.la/v1/users"
GRRAPH_ID = "graph1"

# ------------ Create a User --------------------
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"

}
# response = requests.post(url=endpoint, json=params)
# print(response.text)

# ------------ Create a Graph --------------------
graph_endpint = f"{endpoint}/{USERNAME}/graphs/"

graph_config = {
    "id": GRRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpint, json=graph_config, headers=headers)
# print(response.text)

# ------------------------- Create a pixel -----------------------
today = datetime.now()
formated_date = today.strftime("%Y%m%d")
print(formated_date)
pixel_config = {
    "date": formated_date,
    "quantity": input("How many Km did you run? ")
}
pixel_endpint = f"{endpoint}/{USERNAME}/graphs/{GRRAPH_ID}"

response = requests.post(url=pixel_endpint, json=pixel_config, headers=headers)
print(response.text)

# ------------ Update a Pixel --------------------

dateChange = datetime(year=2022, month=4, day=2)
formated_date_change = dateChange.strftime("%Y%m%d")
pixel_update = f"{endpoint}/{USERNAME}/graphs/{GRRAPH_ID}/{formated_date_change}"
update_config = {
    "quantity" : "5"
}
# response = requests.put(url=pixel_update, json=update_config,headers=headers)
# print(response.text)

# ------------ Delete a Pixel --------------------

dateDelete = datetime(year=2022, month=5, day=2)
formated_date_Deleted = dateDelete.strftime("%Y%m%d")
pixel_Delete = f"{endpoint}/{USERNAME}/graphs/{GRRAPH_ID}/{formated_date_Deleted}"

# response = requests.delete(url=pixel_Delete, headers=headers)
# print(response.text)