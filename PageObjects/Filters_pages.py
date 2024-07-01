import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Product_pages import Product_page


class Filters:

    filters_name_css = "label[style='cursor: pointer;']"


    def __init__(self,driver):
        self.driver = driver

    def apply_filters(self, filter_name1):
        self.all_filter_names = self.driver.find_elements(By.CSS_SELECTOR, self.filters_name_css)

        for self.filter in self.all_filter_names:
            print(self.filter.text)
            if self.filter.text == filter_name1:
                time.sleep(1)
                self.filter.click()









