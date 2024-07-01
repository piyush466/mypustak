from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseClass:

    def __init__(self,driver):
        self.driver = driver


    def do_click(self, by_locator):
        self.driver.find_element(by_locator).click()


    def send_keys_new(self, by_locator, input):
        self.driver.find_element(by_locator).send_keys(input)


    def get_element_text(self,by_locator):
        self.element = self.driver.find_element(by_locator).text
        return self.element.text





