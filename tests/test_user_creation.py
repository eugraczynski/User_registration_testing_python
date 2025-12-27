from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dataclasses import dataclass
from utils.tools import presence_wait, try_assertion, password_randomizer, field_filler
import pytest
import random


@pytest.mark.usefixtures("chrome_driver_setup")
class TestBasePage:
    def test_base_page_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_matches('https://ecommerce-playground.lambdatest.io/'))
        assert 'https://ecommerce-playground.lambdatest.io/' == self.driver.current_url, 'Main page not loaded'

    def test_base_page_title(self):
        expected_title = 'Your Store'
        actual_title = self.driver.title
        assert expected_title == actual_title, f'\nError: Actual title and expected title are different'

@pytest.mark.usefixtures("chrome_driver_setup")
class TestBasePage2:
    @pytest.mark.xfail(reason="Demonstration of xfail marker")
    def test_base_page_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_matches('https://ecommerce-playground.lambdatest.io/'))
        assert 'https://ecommerce-playground.lambdatest.io/' == self.driver.current_url, 'Main page not loaded'

    def test_base_page_title(self):
        expected_title = 'Your Store'
        actual_title = self.driver.title
        assert expected_title == actual_title, f'\nError: Actual title and expected title are different:'

