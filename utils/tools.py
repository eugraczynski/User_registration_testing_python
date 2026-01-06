from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class GlobalUtilities:
    def presence_wait(driver, locator, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f'Element with locator {locator} not found within {timeout} seconds')
    