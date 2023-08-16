import pytest

from config import Config
from history.pages.page_history import PageHistory


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestHistory:

    def test_make_appointment_from_history_page(self):
        page = PageHistory(self.driver)
        page.open_history()
        page.click_make_appointment()
        case = 'appointment with hospital readmission'
        page.set_appointment_data(case)
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        page.page_helper.assert_equal(confirmation_msg, 'Appointment Confirmation', 'Messages mismatch')

    def test_check_history_appointment(self):
        page = PageHistory(self.driver)
        case = 'appointment with hospital readmission'

        expected_url = Config.BASE_URL + '/index.php#appointment'
        page.ensure_correct_page(expected_url)

        page.set_appointment_data(case)
        page.submit_appointment()
        page.open_history()
        data = page.page_helper.read_appointment_data(case)
        visit_date = data['visit_date']
        fields_to_check = [
            ('facility', 'get_history_facility'),
            ('hospital_readmission', 'get_history_hosp_readmission'),
            ('healthcare_program', 'get_history_program'),
            ('comment', 'get_history_comment')
        ]
        for field, method in fields_to_check:
            actual_value = getattr(page, method)(visit_date)
            expected_value = data[field]
            page.page_helper.assert_equal(actual_value, expected_value, f'{field} mismatch.')
