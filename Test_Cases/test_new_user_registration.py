import random
import string
import time



from selenium import webdriver
from selenium.webdriver.common.by import By

import data.test_data
from PageObjects.registration import Register
from Test_Cases.test_user_login_page import Test_Login


class Test_registration:

    def test_register(self,setup):
            """
            Test case for user registration.
            """
            self.driver = setup
            self.driver.implicitly_wait(20)
            self.register = Register(self.driver)
            self.register.click_login()
            self.register.send_email(data.test_data.enter_new_email)
            self.register.enter_mobile_no(data.test_data.enter_mobile_no)
            self.register.enter_password(data.test_data.enter_password)
            self.register.click_sign_up()
            self.check_name  = self.driver.find_element(By.CSS_SELECTOR, Test_Login().text_match)
            assert self.check_name.text == "Hi! Reader", "Something went wrong"


