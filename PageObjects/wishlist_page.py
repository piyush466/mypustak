import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Wishlist:

    click_on_wishlist_css = "div[class='jsx-313054587 Product_heartdiv__p_poW   null']"
    products_names = 'h3'
    wishlist_click = "div[class='jsx-313054587 round-circle d-flex justify-content-center align-items-center']"


    def __init__(self,driver):
        self.driver = driver


    def click_on_wishlist(self):
        time.sleep(5)
        self.product_names = self.driver.find_elements(By.CSS_SELECTOR, self.products_names)
        self.wishlist_click =  self.driver.find_elements(By.CSS_SELECTOR, self.wishlist_click)

        for self.product_name,self.wish in zip(self.product_names, self.wishlist_click):
            print(self.product_name.text)
            if self.product_name.text == "Book Lost Tales Part 1 His":
                self.wish.click()
                break











