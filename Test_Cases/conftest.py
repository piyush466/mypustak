import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import data.test_data


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "Edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome()
    driver.get(data.test_data.url)

    driver.maximize_window()
    request.cls.driver = driver
    return driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )