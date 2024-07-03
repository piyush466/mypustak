import time

from selenium.webdriver import ActionChains

from PageObjects.new_product_page import Add_product
from PageObjects.wishlist_page import Wishlist
from Test_Cases.test_user_login_page import Test_Login
from data import test_data


class Test_Wishlist:


    def test_product_add_in_wishlist(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        Test_Login.test_login(self, setup)
        self.add_product_page = Add_product(self.driver)
        self.add_product_page.search_product_name(test_data.search_book_name)
        self.wishlist = Wishlist(self.driver)
        self.wishlist.click_on_wishlist(test_data.book_name1)
        self.wishlist.click_on_reader()
        self.wishlist.click_wishlist_product()
        self.wishlist.check_products_are_visible_in_wishlist()

        assert test_data.book_name1 in self.wishlist.added_products, "Product Not in wishlist"











