import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone14")
driver.find_element(By.ID, "nav-search-submit-button").click()

allphones = driver.find_elements(By.CSS_SELECTOR, "span[class='a-size-medium a-color-base a-text-normal']")


for phone in allphones:
    print(phone.text)
    if phone.text == "Apple iPhone 14 (512 GB) - Purple":
        phone.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)

time.sleep(2)
try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    element.click()
    # driver.find_element(By.CSS_SELECTOR, "[id='submit.add-to-cart-announce']").click()
except Exception as E:
    print(E)
time.sleep(3)
