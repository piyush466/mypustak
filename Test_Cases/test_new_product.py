import time

from selenium.webdriver.common.by import By

from PageObjects.login_page import Login
from PageObjects.product_p import Add_product
from PageObjects.product_pages import Product_page
from Test_Cases.test_loginPage import Test_Login


class Test_new_products:


    def test_products_again(self,setup):
        self.driver = setup
        self.product = Add_product(self.driver)
        self.product.search_product("Book")
        time.sleep(3)
        self.product.products_name()
        Login(self.driver).click_on_login()
        Login(self.driver).send_email("piyush.alphabin@gmail.com")
        Login(self.driver).click_proceed()
        time.sleep(2)
        Login(self.driver).send_password("Piyush@123")
        Login(self.driver).click_login()
        self.product.click_on_cart()
        self.product.all_product_names_and_price()
        self.product.asserting_cart_and_products_values()
        assert self.product.price_of_product == self.product.var_price , "Cart Value is not match"
        self.product.click_procced_to_checkout()




















