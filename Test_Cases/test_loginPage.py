import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_page import Login


class Test_Login:
    Title_of_page = "Buy Online Books in India | Second Hand Books | MyPustak"


    def test_login(self, setup):
        self.driver = setup
        self.login = Login(self.driver)
        self.login.click_on_login()

        self.login.send_email("piyush.alphabin@gmail.com")
        self.login.click_proceed()
        self.login.send_password("Piyush@123")
        self.login.click_login()
        # assert self.driver.title == self.Title_of_page , "Title is not match"
