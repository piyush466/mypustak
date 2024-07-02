import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Add_product:

    search_product_css = "form[role='search'] input[class='jsx-7037538209317f08 searchInput']"
    click_on_search_xpath = "(//button[@type='submit'])[1]"
    all_products_names_css = "h3"
    add_to_cart_css = "div[style='position: absolute; bottom: 10px; width: 100%;']"
    add_to_cart2_css = "div[class='jsx-313054587 Product_addtoCartText__hr75M']"
    click_on_cart_css = "span[class='{`${styles.icon}`}']"
    all_products_price_css = "cartBookShippingS"
    get_in_out_id = "CartWalletCheckBox"
    total_price_of_products_id = "Totalpricediv"
    click_proceed_to_checkout_btn_css = ".MuiButton-containedWarning.w-100.py-3 "


    def __init__(self,driver):
        self.driver = driver


    def search_product(self,product_name):
        self.driver.find_element(By.CSS_SELECTOR, self.search_product_css).send_keys(product_name)
        self.driver.find_element(By.XPATH, self.click_on_search_xpath).click()

    def products_name(self):
        self.p_names = self.driver.find_elements(By.CSS_SELECTOR, self.all_products_names_css)
        self.all_product_list = []
        for self.product in self.p_names:
            print(self.product.text)
            self.all_product_list.append(self.product.text)
            if self.product.text == "Books V. Cigarettes":
                self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart_css).click()
                time.sleep(3)
                try:
                    self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart2_css).is_displayed()
                    self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart2_css).click()
                except Exception as E:
                    print(E)
                break

    def click_on_cart(self):
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR , self.click_on_cart_css).click()

    def all_product_names_and_price(self):
        time.sleep(4)
        self.prices_of_product = []
        self.products_price = self.driver.find_elements(By.ID, self.all_products_price_css)
        for self.price in self.products_price:
            # print(self.price.text[-4:])
            self.prices_of_product.append(self.price.text[-4:])

        self.after_removeing_rupees_sign = []
        for self.items in self.prices_of_product:
            self.cleanes = self.items.replace('₹', '').strip()
            self.after_removeing_rupees_sign.append(int(self.cleanes))

        # print(self.after_removeing_rupees_sign)
        self.var_price = 0
        for self.add in self.after_removeing_rupees_sign:
            self.var_price = self.var_price + self.add
        print("cart price value:- ",self.var_price)
        try:
            self.driver.find_element(By.ID, self.get_in_out_id).click()

        except Exception as E:
            print(E)

    def asserting_cart_and_products_values(self):
        self.total_amt= self.driver.find_element(By.ID ,self.total_price_of_products_id)
        self.convert_int = self.total_amt.text.replace('₹', '').strip()
        self.price_of_product = int(self.convert_int)
        print("total price of product:- ",self.price_of_product)

        # assert self.price_of_product == self.var_price, "Value is not match"

    def click_procced_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_proceed_to_checkout_btn_css).click()




















