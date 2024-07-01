import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Registration import Register


class Test_registration:

    def test_register(self,setup):
        self.driver = setup
        self.register = Register(self.driver)
        self.register.click_login()
        self.register.send_email("piyush3@gmail.com")
        self.register.enter_mobile_no("8411878794")
        self.register.enter_password("piyush@123")
        self.register.click_sign_up()


