from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config import Config
from locators import CommonLocators
from profile.pages.page_appointment import PageAppointment


class PageHistory(PageAppointment):

    URL = Config.BASE_URL + '/history.php#history'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.sidebar_menu_loc = CommonLocators.SIDEBAR_MENU
        self.sidebar_history_loc = CommonLocators.SIDEBAR_HISTORY
        self.make_appointment_loc = (By.ID, 'btn-make-appointment')
        self.history_panel_xpath = '//div[@class="panel-heading"][.="{}"]'
        self.history_appointment_xpath = '//ancestor::div[contains(@class, "panel")]//p[@id="{}"]'
        self.history_facility_id = 'facility'
        self.history_hosp_readmission_id = 'hospital_readmission'
        self.history_program_id = 'program'
        self.history_comment_id = 'comment'

    def open_history(self):
        sidebar_menu_btn = self.driver.find_element(*self.sidebar_menu_loc)
        sidebar_menu_btn.click()
        sidebar_history_btn = self.driver.find_element(*self.sidebar_history_loc)
        sidebar_history_btn.click()

    def click_make_appointment(self):
        appointment_btn = self.driver.find_element(*self.make_appointment_loc)
        appointment_btn.click()

    def get_history_facility(self, visit_date: str) -> str:
        target_panel_xpath = self.history_panel_xpath.format(visit_date)
        history_facility_xpath = self.history_appointment_xpath.format(self.history_facility_id)
        history_facility = target_panel_xpath + history_facility_xpath
        history_facility_txt = self.driver.find_element(By.XPATH, history_facility).text
        return history_facility_txt

    def get_history_hosp_readmission(self, visit_date: str) -> str:
        target_panel_xpath = self.history_panel_xpath.format(visit_date)
        history_hosp_readmission_xpath = self.history_appointment_xpath.format(self.history_hosp_readmission_id)
        history_hosp_readmission = target_panel_xpath + history_hosp_readmission_xpath
        history_hosp_readmission_txt = self.driver.find_element(By.XPATH, history_hosp_readmission).text
        return history_hosp_readmission_txt

    def get_history_program(self, visit_date: str) -> str:
        target_panel_xpath = self.history_panel_xpath.format(visit_date)
        history_program_xpath = self.history_appointment_xpath.format(self.history_program_id)
        history_program = target_panel_xpath + history_program_xpath
        history_program_txt = self.driver.find_element(By.XPATH, history_program).text
        return history_program_txt

    def get_history_comment(self, visit_date: str) -> str:
        target_panel_xpath = self.history_panel_xpath.format(visit_date)
        history_comment_xpath = self.history_appointment_xpath.format(self.history_comment_id)
        history_comment = target_panel_xpath + history_comment_xpath
        history_comment_txt = self.driver.find_element(By.XPATH, history_comment).text
        return history_comment_txt
