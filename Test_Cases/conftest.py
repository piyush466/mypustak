import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

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
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        driver = webdriver.Ie()

    else:
        driver = webdriver.Chrome()
    driver.get("https://www.mypustak.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )