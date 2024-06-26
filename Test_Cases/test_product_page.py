import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Product_pages import  Product_page
from Utilities.readproperties import Read_proeprties


class Test_productPage:
    user_email = Read_proeprties.user_email()
    password = Read_proeprties.user_password()
    buttons = "//div[@class='jsx-313054587 BookCard_mainUpperBookDiv__lb5Cu']/div[2]"
    add_to_cart_button1 = "//div[text()='Add to Cart']"
    add_to_cart_button2 = "(//div[text()='Add to Cart'])[2]"
    price_of_product_xpath ="//span[@id='cartBookShippingS']"
    Total_price_of_cart_total = "Totalpricediv"


    def test_verify_cart_value(self,setup):
        self.driver = setup

        self.product_page = Product_page(self.driver)
        self.product_page.search_product("Book")
        self.all_product = self.driver.find_elements(By.XPATH, "//h3")

        self.driver.implicitly_wait(10)
        self.product_list= []
        for self.product in self.all_product:
            self.product_list.append(self.product.text)
        self.allbuttons = self.driver.find_elements(By.XPATH, self.buttons)

        for self.button in self.allbuttons[:4]:
            try:
                self.button.click()
                if self.driver.find_element(By.XPATH, self.add_to_cart_button1).is_displayed():
                    self.cart_button = self.driver.find_element(By.XPATH, self.add_to_cart_button1)
                    self.cart_button.click()
                else:
                    self. driver.find_element(By.XPATH, self.add_to_cart_button2).click()
            except:
                print("Exception Occure")

        self.product_page.click_on_add_to_cart()
        self.product_page.send_email(self.user_email)
        self.product_page.send_password(self.password)
        self.product_page.click_login()
        self.allPrice = self.driver.find_elements(By.XPATH, self.price_of_product_xpath)
        self.pricelist= []
        for self.price in self.allPrice:
            self.new_price = self.price.text[-3:]
            self.pricelist.append(self.new_price)

        # print(self.pricelist)
        for self.amount in range(len(self.pricelist)):
            self.pricelist[self.amount] = self.pricelist[self.amount].replace('₹', '')

        # print(self.pricelist)
        self.current_value= 0
        for self.convert_int in self.pricelist:
            self.current_value = self.current_value + int(self.convert_int)
        # print(self.current_value)

        print("Your Cart total value is:- " , self.current_value)
        self.Total_amount = self.driver.find_element(By.ID, self.Total_price_of_cart_total)
        # print(self.Total_amount.text)
        self.remove_sign = self.Total_amount.text.replace('₹', '')
        # print(self.remove_sign)
        self.convert_int_total_value = int(self.remove_sign)
        print("Your Total value:-", self.convert_int_total_value)

        assert self.convert_int_total_value == self.current_value
        self.product_page.click_on_procced_to_checkout()
        self.driver.quit()































