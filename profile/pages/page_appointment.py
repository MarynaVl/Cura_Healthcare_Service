import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from config import Config


class PageAppointment:

    URL = Config.BASE_URL + '/#appointment'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.facility_loc = (By.ID, 'combo_facility')
        self.hospital_readmission_loc = (By.ID, 'chk_hospotal_readmission')
        self.healthcare_program_xpath = '//input[@id="radio_program_{}"]'
        self.visit_date_loc = (By.ID, 'txt_visit_date')
        self.comment_loc = (By.ID, 'txt_comment')
        self.book_appointment_loc = (By.ID, 'btn-book-appointment')
        self.confirmation_loc = (By.XPATH, '//section[@id="summary"]//h2')
        self.booked_facility_loc = (By.CSS_SELECTOR, 'p#facility')
        self.booked_hosp_readmission_loc = (By.CSS_SELECTOR, 'p#hospital_readmission')
        self.booked_program_loc = (By.CSS_SELECTOR, 'p#program')
        self.booked_visit_date_loc = (By.CSS_SELECTOR, 'p#visit_date')
        self.booked_comment_loc = (By.CSS_SELECTOR, 'p#comment')

    @staticmethod
    def read_appointment_data(case_name: str) -> dict:
        with open('../../data/appointment.json', 'r') as file:
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

    @staticmethod
    def assert_equal(actual, expected, message=None):
        assert actual == expected, f"{message}: expected '{expected}', but got '{actual}'"

    def select_facility(self, value: str) -> None:
        facility_field_select = Select(self.driver.find_element(*self.facility_loc))
        facility_field_select.select_by_value(value)

    def check_hospital_readmission(self, data: str) -> None:
        if data == 'Yes':
            hospital_readmission_field = self.driver.find_element(*self.hospital_readmission_loc)
            if not hospital_readmission_field.is_selected():
                hospital_readmission_field.click()

    def check_healthcare_program(self, program: str) -> None:
        program_loc = self.healthcare_program_xpath.format(program.lower())
        program_field = self.driver.find_element(By.XPATH, program_loc)
        if not program_field.is_selected():
            program_field.click()

    def choose_visit_date(self, date: str) -> None:
        date_field = self.driver.find_element(*self.visit_date_loc)
        date_field.clear()
        date_field.send_keys(date)

    def set_comment(self, comment: str) -> None:
        comment_field = self.driver.find_element(*self.comment_loc)
        comment_field.send_keys(comment)

    def submit_appointment(self):
        submit_btn = self.driver.find_element(*self.book_appointment_loc)
        submit_btn.click()

    def set_appointment_data(self, case_name: str) -> None:
        data = self.read_appointment_data(case_name)
        self.select_facility(data['facility'])
        self.check_hospital_readmission(data['hospital_readmission'])
        self.check_healthcare_program(data['healthcare_program'])
        self.choose_visit_date(data['visit_date'])
        self.set_comment(data['comment'])

    def get_confirmation_msg(self) -> str:
        confirmation = self.driver.find_element(*self.confirmation_loc)
        return confirmation.text

    def get_booked_facility(self) -> str:
        facility = self.driver.find_element(*self.booked_facility_loc)
        return facility.text

    def get_booked_hosp_readmission(self) -> str:
        hosp_readmission = self.driver.find_element(*self.booked_hosp_readmission_loc)
        return hosp_readmission.text

    def get_booked_program(self) -> str:
        program = self.driver.find_element(*self.booked_program_loc)
        return program.text

    def get_booked_visit_date(self) -> str:
        visit_date = self.driver.find_element(*self.booked_visit_date_loc)
        return visit_date.text

    def get_booked_comment(self) -> str:
        comment = self.driver.find_element(*self.booked_comment_loc)
        return comment.text

    def get_date_error_msg(self) -> str:
        date_error = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.visit_date_loc))
        error_msg = date_error.get_attribute('validationMessage')
        return error_msg
