import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Chromedriver = 'C:/PythonDev/chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chromedriver)

driver.get("https://tinder.com/")
#
# time.sleep(5)
# print("Hola")
login = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(2)

fb = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb.click()

driver.window_handles
base_window = driver.window_handles[0]
print(driver.title)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
#
time.sleep(2)
username = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
username.send_keys("7712213449")

password = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password.send_keys("QAzplm1$")
time.sleep(2)
enter = driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
enter.click()
time.sleep(5)
driver.switch_to.window(base_window)
time.sleep(5)

ubicacion = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
ubicacion.click()
time.sleep(5)

oboton = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div/div/div[3]/button[1]')
oboton.click()
time.sleep(5)

cookies = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
time.sleep(3)
while True:
    time.sleep(3)
    try:
        like = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')

        like.click()
        time.sleep(2)
    except:
        print("Button not Found")

# match = /html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button/svg

