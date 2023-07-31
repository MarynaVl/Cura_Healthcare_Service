import pytest

from profile.pages.page_login import PageLogin


@pytest.mark.usefixtures('chrome')
class TestLogin:

    def test_login_positive(self):
        page = PageLogin(self.driver)
        page.open()
        page.set_username_login()
        page.set_password_login()
        page.submit_login()
        expected_url = page.base_url + '/#appointment'
        assert expected_url == self.driver.current_url, 'Login was not successful.'

    def test_login_negative(self):
        pass
