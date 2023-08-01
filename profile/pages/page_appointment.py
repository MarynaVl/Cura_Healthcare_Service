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
        self.comment_loc = (By.ID, 'txt_comment')
        self.book_appointment_loc = (By.ID, 'btn-book-appointment')

    def select_facility(self, value: str) -> None:
        facility_field_select = Select(self.driver.find_element(*self.facility_loc))
        facility_field_select.select_by_value(value)

    def check_hospital_readmission(self) -> None:
        hospital_readmission_field = self.driver.find_element(*self.hospital_readmission_loc)
        if not hospital_readmission_field.is_selected():
            hospital_readmission_field.click()

    def check_healthcare_program(self, program: str) -> None:
        program_loc = self.healthcare_program_xpath.format(program.lower())
        program_field = self.driver.find_element(By.XPATH, program_loc)
        if not program_field.is_selected():
            program_field.click()

    def choose_visit_date(self):
        pass

    def set_comment(self):
        pass

    def submit_appointment(self):
        pass


