import pytest

from profile.pages.page_appointment import PageAppointment


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestAppointment:

    def test_make_appointment(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('appointment without hospital readmission')
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        assert confirmation_msg == 'Appointment Confirmation'

    def test_make_appointment_with_hosp_readmission(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('appointment with hospital readmission')
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        assert confirmation_msg == 'Appointment Confirmation'

    def test_make_appointment_min(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('appointment with min data')
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        assert confirmation_msg == 'Appointment Confirmation'

    def test_make_appointment_negative(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('empty date field')
        page.submit_appointment()
        expected_error_messages = ["Заповніть це поле.", "Please fill out this field.", "Заполните это поле."]
        error_msg = page.get_date_error_msg()
        assert error_msg in expected_error_messages, f"Expected one of {expected_error_messages}, but got '{error_msg}'"
        expected_url = page.URL
        current_url = self.driver.current_url
        assert expected_url == current_url, f"Expected URL '{expected_url}', but got '{self.driver.current_url}'"

    def test_check_booked_data(self):
        pass
