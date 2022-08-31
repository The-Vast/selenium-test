"""
login and send email
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Chrome('Driver/chromedriver')


class MailAction:
    def __init__(self, username, password):
        """Initialize the object instance"""
        # self.driver = webdriver.Chrome('Driver/chromedriver')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
        self.driver.find_element(By.XPATH, '//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
        # sleep(4)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='passwordNext']").click()
        # sleep(10)

    def sendmail(self):
        self.driver.get('https://gmail.com')
        self.driver.find_element(By.XPATH, '//*[@id=":15l"]/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id=":1bn"]')
        self.driver.find_element(By.XPATH, '//*[@id=":1b5"]')
        self.driver.find_element(By.XPATH, '//*[@id=":1cb"]')
        sleep(10)
        # ((JavascriptExecutor) driver).executeScript("document.getElementsByClassName('t_estc')[0].click();")


# def test_login_email():
#     driver.get("https://stackoverflow.com/users/signup")
#     driver.maximize_window()
#     time.sleep(6)
#     # driver.find_element_by_id('username').clear()
#     # driver.find_element_by_id('username').send_keys("tomsmith")
#     # driver.find_element_by_id('password').clear()
#     # driver.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")
#     # driver.find_element_by_xpath('//*[@id="login"]/button').send_keys(Keys.RETURN)
#     input_email = driver.find_element("id", "identifierId")
#     input_email.send_keys("was.sanusi@gmail.com")
#     input_email.send_keys(Keys.RETURN)
#     # driver.find_element(by.Id)
#     time.sleep(6)
#     # driver.close()
myMail = MailAction("was.sanusi@gmail.com", "Sanusisolvent1.")
# myMail.sendmail()
