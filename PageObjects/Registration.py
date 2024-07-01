import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:

    login_btn_css = "button[class='undefined icon']"
    send_email_css = "input[class='MuiInputBase-input MuiInput-input MuiInputBase-inputSizeSmall mui-2duac4']"
    proceed_btn_css = "button.WLoginNavbar_loginButton__M7mhW"
    enter_mo_No_xpath = "(//input)[4]"
    enter_password_xpath = "(//input)[5]"
    click_sign_up_css = "button.loginButton"


    def __init__(self,driver):
        self.driver = driver


    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn_css).click()

    def send_email(self,email):
        self.driver.find_element(By.CSS_SELECTOR, self.send_email_css).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, self.proceed_btn_css).click()

    def enter_mobile_no(self, mobile_no):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.enter_mo_No_xpath).send_keys(mobile_no)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.enter_password_xpath).send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_sign_up_css).click()







