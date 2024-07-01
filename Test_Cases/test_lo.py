from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Base_page import BaseClass


class Test_L(BaseClass):

    click_login = (By.XPATH, "//button[@class='undefined icon']")
    send_email = (By.XPATH, "//input[@type='text']")
    click_proceed = (By.XPATH, "//button[text()='Proceed']")
    send_password = (By.XPATH, "//input[@type='password']")
    click_login = (By.XPATH, "(//button[text()='Login'])[2]")

    def test_do_login_again(self,setup):
        self.driver = setup
        
        self.do_click(self.click_login)
        self.send_keys_new(self.send_email,"Piyush.alphabin@gmail.com")
        self.do_click(self.click_proceed)
        self.send_keys_new(self.send_password, "Piyush@123")
        self.do_click(self.click_login)






