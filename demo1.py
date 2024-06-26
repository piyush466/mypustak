# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get("https://demo.alphabin.co/")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "(//button[text()='Shop Now'])[1]").click()
#
# all_products = driver.find_elements(By.XPATH, "//div[@class='hover:shadow-md group w-[340px] h-[447px] mt-[2rem] hover:bg-[#fff] rounded-[5px] hover:cursor-pointer flex flex-col justify-center items-center relative px-3']")
#
# for product in all_products[3:]:
#     product_names = product.find_element(By.XPATH, "a/div/div/h1").text
#     if product_names in ["Router", "Wireless mouse" ]:
#         action = ActionChains(driver)
#         add_to_cart = product.find_element(By.XPATH, "div[2]/button")
#         action.move_to_element(add_to_cart).perform()
#         # product.find_element(By.XPATH, "div[2]/button").click()
#         add_to_cart.click()
#
# driver.find_element(By.XPATH, "(//div[@class='cursor-pointer hidden lg:flex'])[2]").click()
# driver.find_element(By.XPATH, "//button[text()='CHECKOUT']").click()
# time.sleep(5)



















