import pytest
from selenium import webdriver

# Application URL
BASE_URL = ''


@pytest.fixture(scope="class")
def driver_setup(request):
    driver = webdriver.Chrome('../driver/chromedriver.exe')
    request.cls.driver = driver
    driver.get(BASE_URL)
    driver.maximize_window()

    yield driver

    driver.close()
