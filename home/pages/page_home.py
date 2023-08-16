from selenium.webdriver.remote.webdriver import WebDriver

from config import Config
from helpers import PageHelpers
from locators import CommonLocators
from user_profile.pages.page_appointment import PageAppointment


class PageHome(PageAppointment):

    URL = Config.BASE_URL

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page_helper = PageHelpers(driver)
        self.sidebar_menu_loc = CommonLocators.SIDEBAR_MENU
        self.sidebar_home_loc = CommonLocators.SIDEBAR_HOME

    def open_home(self):
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()
        sidebar_home_btn = self.driver.find_element(*self.sidebar_home_loc)
        sidebar_home_btn.click()

