from selenium.webdriver.common.by import By

class LocatorsBasePage:
    SEARCH_FIELD = (By.ID, 'search')
    CART_BUTTON = (By.ID, 'entry_217825')

class LocatorsNavBar:
    NAV_BAR = (By.ID, 'widget-navbar-217834')
    My_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    LOGIN_OPTION = (By.LINK_TEXT, 'Login')
