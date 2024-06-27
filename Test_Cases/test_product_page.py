import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Product_pages import  Product_page
from Utilities.readproperties import Read_proeprties


class Test_productPage:
    user_email = Read_proeprties.user_email()
    password = Read_proeprties.user_password()
    search_book = Read_proeprties.user_book()
    #This are locators
    All_products = "//h3"
    buttons = "//div[@class='jsx-313054587 BookCard_mainUpperBookDiv__lb5Cu']/div[2]"
    add_to_cart_button1 = "//div[text()='Add to Cart']"
    add_to_cart_button2 = "(//div[text()='Add to Cart'])[2]"
    price_of_product_xpath ="//span[@id='cartBookShippingS']"
    Total_price_of_cart_total = "Totalpricediv"
    offer_product_price_xpath = "//span[@style='color: rgb(0, 0, 0); font-weight: bold;']"
    click_on_want_book = "//button[text()='Yes , I want this book']"


    def test_verify_cart_value(self,setup):
        self.driver = setup
        self.product_page = Product_page(self.driver)
        self.product_page.search_product(self.search_book)
        self.all_product = self.driver.find_elements(By.XPATH, self.All_products)

        self.driver.implicitly_wait(10)
        #adding the product in list
        self.product_list= []
        for self.product in self.all_product:
            self.product_list.append(self.product.text)

        #Add to card buttons
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
                None


        #click on ad to cart
        self.product_page.click_on_add_to_cart()
        #Enter Email
        self.product_page.send_email(self.user_email)
        #Enter Password
        self.product_page.send_password(self.password)
        #click on Login button
        self.product_page.click_login()

        #store the product price in list
        self.allPrice = self.driver.find_elements(By.XPATH, self.price_of_product_xpath)
        self.pricelist= []


        # if there is any offer product then this is exicute
        try:
            self.offer_price = self.driver.find_element(By.XPATH, self.offer_product_price_xpath)
            self.remove_rupees_sign = self.offer_price.text.replace('₹', '')
            self.offer_price_book = int(self.remove_rupees_sign)
            print(self.offer_price_book)#offer product price

        except:
            print("exception Occure2")

        #getting the price of product (only last 3 digits)
        for self.price in self.allPrice:
            self.new_price = self.price.text[-3:]
            self.pricelist.append(self.new_price)

        #remove the ruppes sign
        for self.amount in range(len(self.pricelist)):
            self.pricelist[self.amount] = self.pricelist[self.amount].replace('₹', '')
        # print(self.pricelist)

        #Adding the total price of products
        self.current_value= 0
        if self.driver.find_element(By.XPATH, self.offer_product_price_xpath).is_displayed():
            for self.convert_int in self.pricelist:
                self.price_int = int(self.convert_int)
                self.current_value = self.current_value + self.price_int
                self.offer_and_current_value = self.current_value + self.offer_price_book
            print("Sum of offer book and without offer book :", self.offer_and_current_value)

        else:
            for self.convert_int in self.pricelist:
                self.current_value = self.current_value + self.price_int

        #cart Total price display
        print("Your Cart total value is:- ", self.offer_and_current_value)

        self.Total_amount = self.driver.find_element(By.ID, self.Total_price_of_cart_total)
        #removing again ruppes sign
        self.remove_sign = self.Total_amount.text.replace('₹', '')

        self.convert_int_total_value = int(self.remove_sign)
        #Total price
        print("Your Total value:-", self.convert_int_total_value)
        #comparing the both price
        assert self.convert_int_total_value == self.offer_and_current_value, "value is not matching"
        self.product_page.click_on_procced_to_checkout()

        time.sleep(4)
        self.driver.quit()
































