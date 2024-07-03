import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.registration import Register


class Test_registration:
    """
        Test class for the registration process.
        """
    EMAIL = "piyush580@gmail.com"
    MOBILE_NO = "8411878794"
    PASSWORD = "piyush@123"


def test_register(self,setup):
        """
        Test case for user registration.
        """
        self.driver = setup
        self.register = Register(self.driver)
        self.register.click_login()
        self.register.send_email(self.enter_new_email)
        self.register.enter_mobile_no(self.enter_mobile_no)
        self.register.enter_password(self.enter_password)
        self.register.click_sign_up()


