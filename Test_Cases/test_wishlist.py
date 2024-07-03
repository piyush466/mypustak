import time

from selenium.webdriver import ActionChains

from PageObjects.product_p import Add_product
from PageObjects.wishlist_page import Wishlist
from Test_Cases.test_loginPage import Test_Login


class Test_Wishlist:
    book_name = "Book Lost Tales Part 1 His"

    def test_product_add_in_wishlist(self,setup):
        self.driver = setup
        Test_Login.test_login(self, setup)
        self.add_product_page = Add_product(self.driver)
        self.add_product_page.search_product_name("book")
        time.sleep(2)
        self.wishlist = Wishlist(self.driver)
        self.wishlist.click_on_wishlist(self.book_name)
        self.wishlist.click_on_reader()
        self.wishlist.click_wishlist_product()
        time.sleep(2)
        self.wishlist.check_products_are_visible_in_wishlist()
        assert self.book_name in self.wishlist.added_products, "Not in wishlist"










