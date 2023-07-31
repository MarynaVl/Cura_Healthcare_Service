import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageLogin:

    base_url = 'https://katalon-demo-cura.herokuapp.com'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.sidebar_menu_loc = (By.XPATH, '//i[contains(@class, "fa-bars")]')
        self.sidebar_login_loc = (By.XPATH, '//a[text()="Login"]')
        self.username_loc = (By.ID, 'txt-username')
        self.password_loc = (By.ID, 'txt-password')
        self.login_btn_loc = (By.ID, 'btn-login')

    def open(self) -> None:
        self.driver.get(self.base_url)
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()
        sidebar_login_btn = self.driver.find_element(*self.sidebar_login_loc)
        sidebar_login_btn.click()
        expected_url = self.base_url + '/profile.php#profile'
        WebDriverWait(self.driver, timeout=5).until(ec.url_changes(expected_url))

    def set_username_login(self):
        with open('../../data/user.json', 'r') as file:
            data = json.load(file)
        for user_case in data:
            if user_case.get('credential') == 'valid user credential':
                valid_username = user_case['username']
                break
        else:
            raise ValueError('Valid user not found in the JSON user data.')
        username_field = self.driver.find_element(*self.username_loc)
        username_field.clear()
        username_field.send_keys(valid_username)

    def set_password_login(self):
        with open('../../data/user.json', 'r') as file:
            data = json.load(file)
        for user_case in data:
            if user_case.get('credential') == 'valid user credential':
                valid_password = user_case['password']
                break
        else:
            raise ValueError('Valid user case not found in the JSON user data.')
        password_field = self.driver.find_element(*self.password_loc)
        password_field.clear()
        password_field.send_keys(valid_password)

    def submit_login(self):
        submit_btn = self.driver.find_element(*self.login_btn_loc)
        submit_btn.click()
