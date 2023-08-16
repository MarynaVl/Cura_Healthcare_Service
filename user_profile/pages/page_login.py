import json
import importlib.resources as resources

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from config import Config
from helpers import WaitHelper
from locators import CommonLocators


class PageLogin:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait_helper = WaitHelper(driver)
        self.sidebar_menu_loc = CommonLocators.SIDEBAR_MENU
        self.sidebar_login_loc = CommonLocators.SIDEBAR_LOGIN
        self.sidebar_logout_loc = CommonLocators.SIDEBAR_LOGOUT
        self.username_loc = (By.ID, 'txt-username')
        self.password_loc = (By.ID, 'txt-password')
        self.login_btn_loc = (By.ID, 'btn-login')
        self.error_message_loc = (By.CSS_SELECTOR, '.text-danger')
        self.user_json_path = resources.files('data') / 'user.json'

    def open(self) -> None:
        self.driver.get(Config.BASE_URL)
        self.wait_helper.wait_for_visibility(self.sidebar_menu_loc)
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()

        try:
            logout_btn = self.driver.find_element(*self.sidebar_logout_loc)
            logout_btn.click()
            sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
            sidebar_menu_btn.click()
        except NoSuchElementException:
            pass  # The Logout element is missing, the user is not authorized

        self.wait_helper.wait_for_visibility(self.sidebar_login_loc)
        sidebar_login_btn = self.driver.find_element(*self.sidebar_login_loc)
        sidebar_login_btn.click()
        expected_url = Config.BASE_URL + '/profile.php#profile'
        self.wait_helper.wait_for_url_changes(expected_url)

    def set_login_data(self, case: str) -> None:
        with self.user_json_path.open() as file:
            data = json.load(file)
        for user_case in data:
            if user_case.get('credential') == case:
                username = user_case['username']
                password = user_case['password']
                break
        else:
            raise ValueError('Data not found in the JSON user data.')
        self.wait_helper.wait_for_visibility(self.username_loc)
        username_field = self.driver.find_element(*self.username_loc)
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.driver.find_element(*self.password_loc)
        password_field.clear()
        password_field.send_keys(password)

    def submit_login(self):
        submit_btn = self.driver.find_element(*self.login_btn_loc)
        submit_btn.click()

    def get_login_error(self) -> str:
        error_field = self.driver.find_element(*self.error_message_loc)
        return error_field.text
