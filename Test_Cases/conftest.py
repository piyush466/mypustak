import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.mypustak.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

