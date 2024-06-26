import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:

    click_on_login_Xpath = "//button[@class='undefined icon']"
    send_email_xpath = "//input[@type='text']"
    click_proceed_xpath = "//button[text()='Proceed']"
    send_passwod_xpath = "//input[@type='password']"
    click_login_xpath = "(//button[text()='Login'])[2]"


    def __init__(self,driver):
        self.driver = driver

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.click_on_login_Xpath).click()

    def send_email(self,email):
        self.driver.find_element(By.XPATH, self.send_email_xpath).send_keys(email)

    def click_proceed(self):
        self.driver.find_element(By.XPATH, self.click_proceed_xpath).click()

    def send_password(self,password):
        self.driver.find_element(By.XPATH, self.send_passwod_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.click_login_xpath).click()