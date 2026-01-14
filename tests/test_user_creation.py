import time
from typing import ClassVar
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Chrome
from utils.tools import GlobalUtilities 
from page.basepage.mainpage import LocatorsBasePage
from page.basepage.mainpage import LocatorsNavBar
import pytest



@pytest.mark.usefixtures("chrome_driver_setup")
class TestBasePage:
    # driver: Chrome
    def test_base_page_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_matches('https://ecommerce-playground.lambdatest.io/'))
        assert 'https://ecommerce-playground.lambdatest.io/' == self.driver.current_url, 'Main page not loaded'

    def test_base_page_title(self):
        expected_title = 'Your Store'
        actual_title = self.driver.title
        assert expected_title == actual_title, f'\nError: Actual title and expected title are different'


# @pytest.mark.usefixtures("chrome_driver_setup", "firefox_driver_setup")
@pytest.mark.usefixtures("chrome_driver_setup")
class TestVariousElements:
    driver: Chrome
    def test_search_field_presence(self):
        GlobalUtilities.presence_wait(self.driver, LocatorsBasePage.SEARCH_FIELD)

    def test_cart_button_presence(self):
        GlobalUtilities.presence_wait(self.driver, LocatorsBasePage.CART_BUTTON)

    def test_my_account_dropdown_presence(self):
        GlobalUtilities.presence_wait(self.driver, LocatorsNavBar.My_ACCOUNT_DROPDOWN)
    
    def test_actions_chain_example(self):
        account_dropdown = self.driver.find_element(*LocatorsNavBar.My_ACCOUNT_DROPDOWN)
        actions = ActionChains(self.driver)
        actions.move_to_element(account_dropdown).perform()
        time.sleep(2)  # Just for demonstration purposes; avoid using sleep in real tests
# //div[contains(@class, 'Title')][text()='Last']/following-sibling::div//input[@class='number-input']
# contains szuka osobno kazda czesc tekstu

@pytest.mark.usefixtures("chrome_driver_setup")
class TestFailBasePage:
    @pytest.mark.xfail(reason="Demonstration of xfail marker")
    def test_base_page_load(self):
        WebDriverWait(self.driver, 20).until(EC.url_matches('https://ecommerce-playground.lambdatest.io/'))
        assert 'https://ecommerce-playground.lambdatest.io/' == self.driver.current_url, f'\nMain page not loaded'
