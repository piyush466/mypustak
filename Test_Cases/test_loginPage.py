import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_page import Login


class Test_Login:
    text_match = "span[style='display: flex; align-items: center;']"


    def test_login(self, setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.login.click_on_login()

        self.login.send_email("piyush.alphabin@gmail.com")
        self.login.click_proceed()
        self.login.send_password("Piyush@123")
        self.login.click_login()
        self.text  = self.driver.find_element(By.CSS_SELECTOR, self.text_match).text
        assert self.text == "Hi! Reader", "Something went wrong"

