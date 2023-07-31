import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageLogin:

    base_url = 'https://katalon-demo-cura.herokuapp.com'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.sidebar_menu_loc = (By.XPATH, '//i[contains(@class, "fa-bars")]')
        self.sidebar_login_loc = (By.XPATH, '//a[text()="Login"]')
        self.username_loc = (By.ID, '#txt-username')
        self.password_loc = (By.ID, '#txt-password')
        self.login_btn_loc = (By.ID, '#btn-login')

    def open(self) -> None:
        self.driver.get(self.base_url)
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()
        sidebar_login_btn = self.driver.find_element(*self.sidebar_login_loc)
        sidebar_login_btn.click()
        current_url = self.driver.current_url
        expected_url = self.base_url + '/profile.php#login'
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def set_username_login(self):
        with open('data/user.json', 'r') as file:
            data = json.load(file)
        for user in data:
            if user.get('credential') == 'valid user credential':
                valid_username = user['username']
        else:
            raise ValueError('Valid user not found in the JSON user data.')

        username_field = self.driver.find_element(*self.username_loc)
        username_field.clear()
        username_field.send_keys(valid_username)

    def set_password_login(self):
        pass

    def submit_login(self):
        pass
