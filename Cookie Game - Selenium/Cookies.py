from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard
import time

Chromedriver = 'C:/PythonDev/chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chromedriver)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")
min = 100
itemsBuy = {
    "buyCursor": 0,
    "buyGrandma": 0,
    "buyFactory": 0,
    "buyMine": 0,
    "buyShipment": 0,
    "buyAlchemy lab": 0,
    "buyPortal": 0,
    "buyTime machine": 0
}

itemsRelation = {
    "buyCursor": 0,
    "buyGrandma": 0,
    "buyFactory": 0,
    "buyMine": 0,
    "buyShipment": 0,
    "buyAlchemy lab": 0,
    "buyPortal": 0,
    "buyTime machine": 0
}
cookieSecond = [0.2, 0.8, 4, 10, 20, 100, 200, 500]


def getMoney():

    try:
        totalCookies = driver.find_element(by=By.ID, value="money").text.replace(',', '')
        # print(totalCookies)
        return int(totalCookies)
    except:
        print("Fail in Get money")

def getPrice():
    for item, value in itemsBuy.items():
        try:
            price = driver.find_element(by=By.ID, value=item)
            finalPrice = int(price.text.split("-")[1].split()[0].replace(',', ''))
            itemsBuy[item] = finalPrice
        except:
            print("Failed in get price")
    #     print(item, value)
    # print(itemsBuy)


def buyItem(item):
    try:
        itemToBuy = driver.find_element(by=By.ID, value=item)
        itemToBuy.click()
    except:
        print("Failed to buy")


def itemToBuy():
    getPrice()
    i = 0
    toB = ""
    min = 123456789
    # print(min)
    for item, value in itemsBuy.items():
        rel = value / cookieSecond[i]
        itemsRelation[item] = rel
        if rel < min:
            min = rel
            toB = item
        i += 1
    print(f"next item to buy is {toB}")
    # print(itemsRelation)
    return toB


def Click():
    for i in range(0, 200):
        cookie.click()


def canBuy(item):
    money = getMoney()
    if money >= itemsBuy[item]:
        buyItem(item)
        print(f"I bougth {item} ")
    else:
        print(f"I want to buy {item}, still have no money")

timeout = time.time() + 5
five_min = time.time() + 60*10 # 5minutes
while True:
    # if keyboard.read_key() == "p":
    Click()
    # Every 5 seconds:
    if time.time() > timeout:
        a = itemToBuy()
        canBuy(a)
        # Add another 5 seconds until the next check
        timeout = time.time() + 3
    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

