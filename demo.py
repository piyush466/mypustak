import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mypustak.com/")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "(//input[@placeholder='Search for books by title, author, Publication or ISBN '])[1]").send_keys("Book")
driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()

allbuttons = driver.find_elements(By.XPATH ,"//div[@class='jsx-313054587 BookCard_mainUpperBookDiv__lb5Cu']/div[2]")

for button in allbuttons[:5]:
    try:
        button.click()
        # cart_button = driver.find_element(By.XPATH, "//div[text()='Add to Cart']").is_displayed()
        if driver.find_element(By.XPATH, "//div[text()='Add to Cart']").is_displayed():
            cart_button = driver.find_element(By.XPATH, "//div[text()='Add to Cart']")
            cart_button.click()
        else:
            driver.find_element(By.XPATH, "(//div[text()='Add to Cart'])[2]").click()


        time.sleep(2)
    except:
        print("exception")




time.sleep(10)


