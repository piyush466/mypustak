from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_page:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).click()


    def send_keys1(self, by_locator, input):

        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(by_locator))).send_keys(input)
        # self.driver.find_element(by_locator).send_keys(input)
    def get_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title
