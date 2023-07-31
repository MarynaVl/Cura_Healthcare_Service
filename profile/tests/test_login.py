import pytest

from profile.pages.page_login import PageLogin


@pytest.mark.usefixtures('chrome')
class TestLogin:

    def test_login_positive(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_username_login('valid user credential')
        page.set_password_login('valid user credential')
        page.submit_login()
        expected_url = page.base_url + '/#appointment'
        assert expected_url == self.driver.current_url, 'Login was not successful.'

    def test_login_with_invalid_username(self):
        page = PageLogin(self.driver)
        page.open()
        page.open()
        page.set_username_login('invalid username')
        page.set_password_login('invalid username')
        page.submit_login()
        assert page.get_login_error() == 'Login failed! Please ensure the username and password are valid.'

