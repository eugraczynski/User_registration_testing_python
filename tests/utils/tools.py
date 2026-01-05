from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import string
import random


# option 1
def presence_wait(driver, locator):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator))
        element = driver.find_element(*locator)
        return element
    except TimeoutError:
        raise Exception(f'Element with locator: {locator} - timeout')


def field_filler(driver, field_locator, data):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(field_locator)).send_keys(data)


def assertion(actual_result, expected_result):
    assert actual_result == expected_result, '\nError: Actual result and expected result are different:' \
                                             f'\nActual:{actual_result}\nExpected:{expected_result}'
