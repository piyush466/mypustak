import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.filters_pages import Filters
from PageObjects.product_pages import Product_page


class Test_Filters:

    filter_select = "Pegasus(361)"

    def test_filter_page(self,setup):

        self.driver= setup
        self.driver.implicitly_wait(10)
        self.profduct_page = Product_page(self.driver)
        self.profduct_page.search_product("Book")
        self.filters= Filters(self.driver)
        self.filters.apply_filters(self.filter_select)
        assert self.filters.checkbox_is_selected == True, 'Checkbox is not selected'











