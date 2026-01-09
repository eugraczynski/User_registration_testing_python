from selenium.webdriver.common.by import By

class LocatorsBasePage:
    SEARCH_FIELD = (By.ID, 'search')
    CART_BUTTON = (By.ID, 'entry_217825')

class LocatorsNavBar:
    My_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "a[@title='My Account']")
    LOGIN_OPTION = (By.ID, "a[href='https://ecommerce-playground.lambdatest.io/index.php?route=account/login']")
