import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.login_page import Login
from PageObjects.wishlist_page import Wishlist
from Test_Cases.test_user_login_page import Test_Login


class Test_Logout:
    logout = "(//div[@style='display: block; padding: 0.7rem 1rem 0rem; text-decoration: none; cursor: pointer;'])[8]"

    def test_user_can_logout(self, setup):
        self.driver = setup
        self.login_test = Test_Login()
        self.login_test.setup = self.driver  # Set the setup for Test_Login instance
        self.login_test.test_login(self.driver)
        time.sleep(2)
        Wishlist(self.driver).click_on_reader()
        self.driver.find_element(By.XPATH, self.logout).click()
        time.sleep(3)
        self.text_login = self.driver.find_element(By.CSS_SELECTOR, Login(self.driver).click_on_login_css).text
        assert  self.text_login == "Login" , "Logout unsuccesfull"


