import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.registration import Register


class Test_registration:
    enter_new_email = "piyush57@gmail.com"
    enter_mobile_no = "8411878794"
    enter_password = "piyush@123"

    def test_register(self,setup):
        self.driver = setup
        self.register = Register(self.driver)
        self.register.click_login()
        self.register.send_email(self.enter_new_email)
        self.register.enter_mobile_no(self.enter_mobile_no)
        self.register.enter_password(self.enter_password)
        self.register.click_sign_up()


