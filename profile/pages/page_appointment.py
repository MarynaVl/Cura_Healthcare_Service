import datetime
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class PageAppointment:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.facility_loc = (By.ID, 'combo_facility')
        self.hospital_readmission_loc = (By.ID, 'chk_hospotal_readmission')
        self.healthcare_program_xpath = '//input[@id="radio_program_{}"]'
        self.visit_date_loc = (By.ID, 'txt_visit_date')
        self.datepicker_loc = (By.CSS_SELECTOR, '.datepicker')
        self.comment_loc = (By.ID, 'txt_comment')
        self.book_appointment_loc = (By.ID, 'btn-book-appointment')
        self.confirmation_loc = (By.CSS_SELECTOR, 'p.lead')

    def select_facility(self, value: str) -> None:
        facility_field_select = Select(self.driver.find_element(*self.facility_loc))
        facility_field_select.select_by_value(value)

    def check_hospital_readmission(self, boolean: bool) -> None:
        if boolean:
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
        if date == 'current day':
            current_date = datetime.datetime.now().strftime("%d/%m/%Y")
            date_field.send_keys(current_date)
        else:
            date_field.send_keys(date)

    def set_comment(self, comment: str) -> None:
        comment_field = self.driver.find_element(*self.comment_loc)
        comment_field.send_keys(comment)

    def submit_appointment(self):
        submit_btn = self.driver.find_element(*self.book_appointment_loc)
        submit_btn.click()

    def set_appointment_data(self, case_name: str) -> None:
        with open('../../data/appointment.json', 'r') as file:
            data = json.load(file)
        for case in data:
            if case.get('info') == case_name:
                facility = case['facility']
                hospital_readmission = case['hospitalReadmission']
                healthcare_program = case['healthcareProgram']
                visit_date = case['date']
                comment = case['comment']
                break
        else:
            raise ValueError('Data not found in the JSON appointment data.')
        self.select_facility(facility)
        self.check_hospital_readmission(hospital_readmission)
        self.check_healthcare_program(healthcare_program)
        self.choose_visit_date(visit_date)
        self.set_comment(comment)
