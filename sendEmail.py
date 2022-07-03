"""
login and send email
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_login_email():
    driver.get('https://www.gmail.com')
    driver.maximize_window()
    input_email = driver.find_element(By.ID, 'identifierId')
    input_email.send_keys("was.sanusi@gmail.com")
    # input_email.send_keys(Keys.RETURN)
    time.sleep(6)
    # driver.close()

