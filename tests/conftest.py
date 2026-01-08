import pytest
from selenium import webdriver

# Application URL
BASE_URL = 'https://ecommerce-playground.lambdatest.io/'


@pytest.fixture(scope="class")
def chrome_driver_setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.implicitly_wait(2)
    driver.get(BASE_URL)
    driver.maximize_window()

    yield driver

    driver.close()

@pytest.fixture()
def firefox_driver_setup(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(2)
    driver.get(BASE_URL)
    driver.maximize_window()

    yield driver

    driver.close()
