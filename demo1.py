from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://www.mypustak.com/")

    # Add your login steps here if required

    # Navigate to the product page (replace with actual product URL or logic to find the product)
    product_url = "https://www.mypustak.com/sample-product"
    driver.get(product_url)

    # Wait until the wishlist button is available and check its status
    wait = WebDriverWait(driver, 10)
    wishlist_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wishlist-button-class")))

    # Check if the product is already in the wishlist
    try:
        # Adjust the logic to determine if the product is already in the wishlist
        if "Added to Wishlist" in wishlist_button.text:
            print("Product already in wishlist")
        else:
            wishlist_button.click()
            print("Product added to wishlist")
    except NoSuchElementException:
        print("Wishlist button not found or some other error")

finally:
    # Close the WebDriver
    driver.quit()