import json
import importlib.resources as resources

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WaitHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_for_url_changes(self, expected_url: str, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_changes(expected_url))


class PageHelpers:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def assert_equal(actual, expected, message=None):
        assert actual == expected, f"{message}: expected '{expected}', but got '{actual}'"

    @staticmethod
    def read_appointment_data(case_name: str) -> dict:
        appointment_json_path = resources.files('data') / 'appointment.json'
        with appointment_json_path.open() as file:
            data = json.load(file)
        for case in data:
            if case.get('info') == case_name:
                return {
                    'facility': case['facility'],
                    'hospital_readmission': case['hospitalReadmission'],
                    'healthcare_program': case['healthcareProgram'],
                    'visit_date': case['date'],
                    'comment': case['comment']
                }
        else:
            raise ValueError('Data not found in the JSON appointment data.')
