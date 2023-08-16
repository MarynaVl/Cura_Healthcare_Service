import pytest

from config import Config
from user_profile.pages.page_logout import PageLogout


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestLogout:

    def test_logout(self):
        page = PageLogout(self.driver)
        page.sidebar_logout()
        expected_url = Config.BASE_URL
        assert expected_url == self.driver.current_url.rstrip('/'), 'Logout was not successful.'
