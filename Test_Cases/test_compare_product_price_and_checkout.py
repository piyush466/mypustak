import time

from selenium.webdriver.common.by import By

import data.test_data
from PageObjects.login_page import Login
from PageObjects.new_product_page import Add_product
from PageObjects.product_pages import Product_page
#from Test_Cases.test_loginPage import Test_Login


class Test_new_products:

    def test_add_cart_and_match_values_products_again(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.product = Add_product(self.driver)
        self.product.search_product_name(data.test_data.search_book_name)
        self.product.products_names()
        Login(self.driver).click_on_login()
        Login(self.driver).send_email(data.test_data.email1)
        Login(self.driver).click_proceed()
        Login(self.driver).send_password(data.test_data.password)
        Login(self.driver).click_login()
        self.product.click_on_cart()
        self.product.all_product_names_and_price()
        self.product.asserting_cart_and_products_values()

        #Adding the all products price and comparing with proceed page price
        assert self.product.price_of_product == self.product.var_price, "Cart Value is not match"
        self.product.click_procced_to_checkout()





















