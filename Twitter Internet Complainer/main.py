import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Chromedriver = 'C:/PythonDev/chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chromedriver)


def twiter ():
    driver.get("https://www.twitter.com/i/flow/login")
    time.sleep(5)
    print("Hola")
    mail = driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    mail.send_keys("mura.ivan@hotmail.com")
    mail.send_keys(Keys.ENTER)
    time.sleep(5)
    # user = driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    # user.send_keys("mura_ivan")
    # user.send_keys(Keys.ENTER)
    # time.sleep(5)
    password = driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys("A01272614")
    password.send_keys(Keys.ENTER)
    time.sleep(3)


def get_internet_speed():
    driver.get("https://www.speedtest.net/")

    # Depending on your location, you might need to accept the GDPR pop-up.
    # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
    # accept_button.click()

    time.sleep(3)
    go_button = driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
    go_button.click()

    time.sleep(60)
    up = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    down = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    print(up,down)

get_internet_speed()