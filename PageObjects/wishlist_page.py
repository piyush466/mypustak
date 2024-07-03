import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Wishlist:

    # click_on_wishlist_css = "div[class='jsx-313054587 Product_heartdiv__p_poW   null']"
    products_names = 'h3'
    wishlist_click = "div[class='jsx-313054587 round-circle d-flex justify-content-center align-items-center']"
    click_on_hi_reader_css = "span[style='display: flex; align-items: center;']"
    click_on_wishlist_css2_from_list = '[data-testid="ListOutlinedIcon"]'
    wishlish_products = "[class='jsx-699a0f249084c2b3 Wishlist_wishTitle__2np5k']"

    def __init__(self,driver):
        self.driver = driver


    def click_on_wishlist(self,book_name):
        time.sleep(5)
        #//h3[@title='BOOK KEEPING AND ACCOUNTANCY']//ancestor::div[contains(@class, 'jsx-3')]//div[contains(@class, '313054587 Product_h')]
        self.heart_click = self.driver.find_element(By.XPATH, f"//h3[@title='{book_name}']"
                                           "//ancestor::div[contains(@class, 'jsx-3')]//div[contains(@class, '313054587 Product_h')]")
        self.heart_click.click()

    def click_on_reader(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_hi_reader_css).click()

    def click_wishlist_product(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_wishlist_css2_from_list).click()

    def check_products_are_visible_in_wishlist(self):
        time.sleep(4)
        self.wishlist_products_text = self.driver.find_elements(By.CSS_SELECTOR, self.wishlish_products)
        self.added_products = []
        for self.wishlist_product in self.wishlist_products_text:
            self.all_wish_product_text = self.wishlist_product.text
            self.added_products.append(self.all_wish_product_text)

        # print(self.added_products)


















