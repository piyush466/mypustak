import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:

    click_on_login_css = "button[class='undefined icon']"
    send_email_css = "input.MuiInputBase-input "
    click_proceed_css = "button.WLoginNavbar_loginButton__M7mhW"
    send_passwod_css = "input[type='password']"
    click_login_css = "button.WLoginNavbar_loginButton__M7mhW"


    def __init__(self,driver):
        self.driver = driver

    def click_on_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_login_css).click()

    def send_email(self,email):
        self.driver.find_element(By.CSS_SELECTOR, self.send_email_css).send_keys(email)

    def click_proceed(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_proceed_css).click()

    def send_password(self,password):
        self.driver.find_element(By.CSS_SELECTOR, self.send_passwod_css).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_login_css).click()

