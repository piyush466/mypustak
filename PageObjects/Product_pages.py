import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Product_page:

    search_product_CSS = "form[role='search'] input[class='jsx-7037538209317f08 searchInput']"
    click_on_search_xpath = "(//button[@type='submit'])[1]"
    all_products_css = "h3"
    click_on_add_to_cart_xpath = "(//span[text()='Cart'])[1]"
    # click_cart_xpath ="(//span[@class='MuiBadge-root mui-1rzb3uu'])[1]"
    email_Id_for_login  = "login_email"
    proceed_btn_css= "button[class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth mui-6c44q9']"
    password_id = "login_password"
    click_login_css = "button[class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth mui-6c44q9']"
    price_verify_css  = ".fw-bold "
    proceed_to_checkout_css = "button[class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedWarning MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedWarning MuiButton-sizeMedium MuiButton-containedSizeMedium w-100 py-3 text-white shadow mui-ypa2qc']"
    offer_product_price_css = "span[style='color: rgb(0, 0, 0); font-weight: bold;']"
    click_on_want_book = "button[class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium mui-2nafv5']"

    def __init__(self,driver):
        self.driver =driver

    def search_product(self, produc_name):
        self.driver.find_element(By.CSS_SELECTOR, self.search_product_CSS).send_keys(produc_name)
        self.driver.find_element(By.XPATH, self.click_on_search_xpath).click()


    def handle_windows(self):
        self.window = self.driver.window_handles
        self.driver.switch_to.window(self.window[1])

    def click_on_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.click_on_add_to_cart_xpath).click()
        # self.driver.find_element(By.XPATH, self.click_cart_xpath).click()

    def send_email(self,email):
        self.driver.find_element(By.ID, self.email_Id_for_login).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, self.proceed_btn_css).click()

    def send_password(self,password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_login_css).click()

    def click_on_procced_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.proceed_to_checkout_css).click()
        self.driver.find_element(By.XPATH, self.click_on_want_book).click()

    def offer_product(self):
        try:
            self.offer_price = self.driver.find_element(By.XPATH, self.offer_product_price_xpath)
            print(self.offer_price.text)
            self.remove_rupees_sign = self.offer_price.text.replace('₹', '')
        except:
            print("exception occure")
























