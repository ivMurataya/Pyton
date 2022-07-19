from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = 'C:/PythonDev/chromedriver.exe'
SIMILAR_ACCOUNT = "vriim360"
USERNAME = "myaccound"
PASSWORD = "password"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)
        followers = self.driver.find_element(by=By.XPATH, value=
            '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(4)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        for i in range(2):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(4)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
                cancel_button.click()






bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()