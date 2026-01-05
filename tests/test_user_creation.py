from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.tools import presence_wait, assertion
import pytest


class LocatorsBasePage:
    SEARCH_FIELD = (By.ID, 'searchs')
    CART_BUTTON = (By.ID, 'entry_217825')

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
class TestVariousElements(LocatorsBasePage):
    def test_search_field_presence(self):
        search_field = presence_wait(self.driver, self.SEARCH_FIELD)
        assert search_field.is_displayed(), 'Search field is not displayed on the main page'

    def test_cart_button_presence(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'entry_217825'))
        )
        assert cart_button.is_displayed(), 'Cart button is not displayed on the main page'

@pytest.mark.usefixtures("chrome_driver_setup")
class TestFailBasePage:
    @pytest.mark.xfail(reason="Demonstration of xfail marker")
    def test_base_page_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_matches('https://ecommerce-playground.lambdatest.io/'))
        assert 'https://ecommerce-playground.lambdatest.io/' == self.driver.current_url, f'\nMain page not loaded'

    def test_base_page_title(self):
        expected_title = 'Your Store'
        actual_title = self.driver.title
        assert expected_title == actual_title, f'\nError: Actual title and expected title are different:'

