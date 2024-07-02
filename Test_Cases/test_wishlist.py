import time

from PageObjects.product_p import Add_product
from PageObjects.wishlist_page import Wishlist
from Test_Cases.test_loginPage import Test_Login


class Test_Wishlist:

    def test_product_add_in_wishlist(self,setup):
        self.driver = setup
        Test_Login.test_login(self, setup)
        self.add_product_page = Add_product(self.driver)
        self.add_product_page.search_product_name("book")
        time.sleep(2)
        self.wishlist = Wishlist(self.driver)
        self.wishlist.click_on_wishlist()








