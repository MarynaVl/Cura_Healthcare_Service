import pytest

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
        page.assert_equal(confirmation_msg, 'Appointment Confirmation', 'Messages mismatch')

    def test_check_history_appointment(self):
        page = PageHistory(self.driver)
        case = 'appointment with hospital readmission'
        page.set_appointment_data(case)
        page.submit_appointment()
        page.open_history()
        data = page.read_appointment_data(case)
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
            page.assert_equal(actual_value, expected_value, f'{field} mismatch.')
