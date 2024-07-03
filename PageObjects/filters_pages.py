import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.product_pages import Product_page


class Filters:

    filters_name_css = "label[style='cursor: pointer;']"


    def __init__(self,driver):
        self.driver = driver

    def apply_filters(self, filter_name1):
        self.all_filter_names = self.driver.find_elements(By.CSS_SELECTOR, self.filters_name_css)
        self.checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        for self.filter, self.checkbox in zip(self.all_filter_names, self.checkboxes):
            print(self.filter.text)
            if self.filter.text == filter_name1:
                time.sleep(1)
                self.filter.click()
                self.checkbox_is_selected = self.checkbox.is_selected()
                break









