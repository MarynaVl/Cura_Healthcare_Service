import pytest

from profile.pages.page_login import PageLogin
from config import Config


@pytest.mark.usefixtures('chrome')
class TestLogin:

    def test_login_positive(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('valid user credential')
        page.submit_login()
        expected_url = Config.BASE_URL + '/#appointment'
        assert expected_url == self.driver.current_url, 'Login was not successful.'

    def test_login_with_invalid_username(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('invalid username')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'

    def test_login_with_invalid_password(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('invalid password')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'

    def test_login_with_empty_fields(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('empty fields')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'

    def test_login_with_empty_username(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('empty username field')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'

    def test_login_with_empty_password(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_login_data('empty password field')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'


