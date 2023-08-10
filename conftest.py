from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from user_profile.pages.page_login import PageLogin


@pytest.fixture(scope='class')
def chrome(request):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def authentication(chrome):
    page = PageLogin(chrome)
    page.open()
    page.set_login_data('valid user credential')
    page.submit_login()
    return chrome
