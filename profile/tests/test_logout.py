import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import Config
from profile.pages.page_logout import PageLogout


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestLogout:

    def test_logout(self):
        page = PageLogout(self.driver)
        page.sidebar_logout()
        expected_url = Config.BASE_URL
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.url_matches(expected_url), 'Logout was not successful.')
