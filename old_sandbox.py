from selenium.webdriver.common.by import By
from utils.tools import presence_wait, try_assertion, password_randomizer, field_filler
import random
from dataclasses import dataclass


# from pathlib import Path
# import sys

# sys.path.append(str(Path(__file__).parent))

# print((Path(__file__).parent.parent))


# Profile URL
PROFILE_URL = ''

# Main page locators
PAGE_USER_PROFILE_BUTTON = (By.ID, '//span[@data-cy="login-icon"]')

# Example of selection of locators with spare spaces, like this "     Create an account       " using normalize-space()
PAGE_CREATE_ACCOUNT_BUTTON = (By.ID, '//button[normalize-space()="Create an account"]')

# Profile locators
PAGE_PROFILE_FIRSTNAME = (By.ID, "//div[@data-testid='firstName']")
PAGE_PROFILE_LASTNAME = (By.ID, '//div[@data-testid="lastName"]')
PAGE_PROFILE_EMAIL = (By.ID, '//div[@data-testid="email"]')

# New user creation form locators
USER_REGISTRATION_FIRST_NAME_FIELD = (By.ID, 'registration-first-name')
USER_REGISTRATION_LAST_NAME_FIELD = (By.ID, 'registration-last-name')
USER_REGISTRATION_PHONE_NUMBER = (By.ID, 'alternativePhoneNumber')
USER_REGISTRATION_EMAIL = (By.ID, 'registrationEmail')
USER_REGISTRATION_PASSWORD = (By.ID, 'registrationPassword')
USER_REGISTRATION_STREET = (By.ID, 'registration-street')
USER_REGISTRATION_ZIPCODE = (By.ID, 'registration-zipcode')
USER_REGISTRATION_CITY = (By.ID, 'registration-city')

# NEVER USE XPATH ... Example for selection of parent element, in case if we need to click the parent
SALUTATION_SELECT = (By.XPATH, '//span[text()="Salutation"]/parent::div')
USER_REGISTRATION_COUNTRY_SELECT = (By.XPATH, '//span[text()="Country"]/parent::div')


# Test data assembler
@dataclass
class UserDataLoader:
    USER_FIRSTNAME: str
    USER_LAST_NAME: str
    USER_PHONE_NUMBER: str
    USER_PASSWORD: str
    USER_EMAIL: str
    USER_STREET: str
    USER_ZIPCODE: str
    USER_CITY: str
    USER_COUNTRY: str
    USER_SALUTATION: str


TestData = UserDataLoader('Jan', 'Kowalski', '48123123123', f'{password_randomizer()}',
                                     f'test{random.randint(0, 9999)}@domain.com', 'Mieszka I 22/8',
                                     '30-412', 'Krakow', 'France', 'Mrs.')



# class TestRegisterNewUser:
#     def test_user_icon_click(self):
#         # User account button click
        # presence_wait(self.driver, PAGE_USER_PROFILE_BUTTON).click()
#         presence_wait(self.driver, PAGE_CREATE_ACCOUNT_BUTTON).click()

#     # Filling user data
#     def test_filling_user_data(self):
#         # Salutation select
#         presence_wait(self.driver, SALUTATION_SELECT).click()
#         self.driver.find_element(By.XPATH, f'//div[normalize-space()="{TestData.USER_SALUTATION}"]').click()

#         # First name fill
        # field_filler(self.driver, USER_REGISTRATION_FIRST_NAME_FIELD, TestData.USER_FIRSTNAME)

#         # Last name fill
#         field_filler(self.driver, USER_REGISTRATION_LAST_NAME_FIELD, TestData.USER_LAST_NAME)

#         # Phone number fill
#         field_filler(self.driver, USER_REGISTRATION_PHONE_NUMBER, f"+{TestData.USER_PHONE_NUMBER}")

#         # Email fill
#         field_filler(self.driver, USER_REGISTRATION_EMAIL, TestData.USER_EMAIL)

#         # Password fill
#         field_filler(self.driver, USER_REGISTRATION_PASSWORD, TestData.USER_PASSWORD)

#         # Street fill
#         field_filler(self.driver, USER_REGISTRATION_STREET, TestData.USER_STREET)

#         # Zipcode fill
#         field_filler(self.driver, USER_REGISTRATION_ZIPCODE, TestData.USER_ZIPCODE)

#         # City fill
#         field_filler(self.driver, USER_REGISTRATION_CITY, TestData.USER_CITY)

#         # Country select
#         presence_wait(self.driver, USER_REGISTRATION_COUNTRY_SELECT).click()
#         self.driver.find_element(By.XPATH, f'//div[normalize-space()="{TestData.USER_COUNTRY}"]').click()

#         # Create account click
#         presence_wait(self.driver, PAGE_CREATE_ACCOUNT_BUTTON).click()

#     def test_user_redirection_to_profile(self):
#         # Check if user was automatically logged in and redirected to profile page
#         WebDriverWait(self.driver, 20).until(EC.url_matches(PROFILE_URL))
#         assert PROFILE_URL == self.driver.current_url, 'Wrong URL, user is not logged'

#     def test_user_data_compare(self):
#         # User data check
#         user_profile_first_name = self.driver.find_element(*PAGE_PROFILE_FIRSTNAME)
#         user_profile_last_name = self.driver.find_element(*PAGE_PROFILE_LASTNAME)
#         user_profile_email = self.driver.find_element(*PAGE_PROFILE_EMAIL)

#         # Assertion calls for firstname, lastname, email user data on profile page
#         try_assertion(user_profile_first_name.get_attribute('value'), TestData.USER_FIRSTNAME)
#         try_assertion(user_profile_last_name.get_attribute('value'), TestData.USER_LAST_NAME)
#         try_assertion(user_profile_email.get_attribute('value'), TestData.USER_EMAIL)

