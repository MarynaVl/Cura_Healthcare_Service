from selenium.webdriver.common.by import By


class CommonLocators:
    SIDEBAR_MENU = (By.XPATH, '//i[contains(@class, "fa-bars")]')
    SIDEBAR_HOME = (By.XPATH, '//a[text()="Home"]')
    SIDEBAR_LOGIN = (By.XPATH, '//a[text()="Login"]')
    SIDEBAR_HISTORY = (By.XPATH, '//a[text()="History"]')
    SIDEBAR_PROFILE = (By.XPATH, '//a[text()="Profile"]')
    SIDEBAR_LOGOUT = (By.XPATH, '//a[text()="Logout"]')
