from selenium.webdriver.remote.webdriver import WebDriver
from locators import CommonLocators


class PageLogout:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.sidebar_menu_loc = CommonLocators.SIDEBAR_MENU
        self.sidebar_logout_loc = CommonLocators.SIDEBAR_LOGOUT

    def sidebar_logout(self):
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()
        sidebar_logout_btn = self.driver.find_element(*self.sidebar_logout_loc)
        sidebar_logout_btn.click()
