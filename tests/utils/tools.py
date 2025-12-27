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
    except NoSuchElementException:
        raise NoSuchElementException


# option 2
# def presence_wait(driver, locator):
#     WebDriverWait(driver, 100).until(
#         lambda driver: driver.find_element_by_name(*locator))
#     element = driver.find_element(*locator)
#     return element


# Adding randomized password
def password_randomizer():
    characters = list(string.ascii_letters + string.digits + "~=.,!@#$%^&*()")
    random.shuffle(characters)
    password = []
    [password.append(random.choice(characters)) for i in range(7)]
    random.shuffle(password)
    return "".join(password)


# Filling fields
def field_filler(driver, field_locator, data):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(field_locator)).send_keys(data)


def try_assertion(actual_result, expected_result):
    assert actual_result == expected_result, '\nError: Actual result and expected result are different:' \
                                             f'\nActual:{actual_result}\nExpected:{expected_result}'
