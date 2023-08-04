import pytest

from profile.pages.page_appointment import PageAppointment


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestAppointment:

    @pytest.mark.smoke
    def test_make_appointment(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('appointment without hospital readmission')
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        assert confirmation_msg == 'Appointment Confirmation'

    def test_appointment_with_hosp_readmission(self):
        case = 'appointment with hospital readmission'
        page = PageAppointment(self.driver)
        page.set_appointment_data(case)
        page.submit_appointment()
        data = page.read_appointment_data(case)
        fields_to_check = [
            ('facility', 'get_booked_facility'),
            ('hospital_readmission', 'get_booked_hosp_readmission'),
            ('healthcare_program', 'get_booked_program'),
            ('visit_date', 'get_booked_visit_date'),
            ('comment', 'get_booked_comment')
        ]
        for field, method in fields_to_check:
            actual_value = getattr(page, method)()
            expected_value = data[field]
            assert actual_value == expected_value, \
                f"{field} mismatch. Expected '{expected_value}', but got '{actual_value}'"

    def test_appointment_without_hosp_readmission(self):
        case = 'appointment without hospital readmission'
        page = PageAppointment(self.driver)
        page.set_appointment_data(case)
        page.submit_appointment()
        data = page.read_appointment_data(case)
        fields_to_check = [
            ('facility', 'get_booked_facility'),
            ('hospital_readmission', 'get_booked_hosp_readmission'),
            ('healthcare_program', 'get_booked_program'),
            ('visit_date', 'get_booked_visit_date'),
            ('comment', 'get_booked_comment')
        ]
        for field, method in fields_to_check:
            actual_value = getattr(page, method)()
            expected_value = data[field]
            assert actual_value == expected_value, \
                f"{field} mismatch. Expected '{expected_value}', but got '{actual_value}'"

    def test_appointment_min(self):
        case = 'appointment with min data'
        page = PageAppointment(self.driver)
        page.set_appointment_data(case)
        page.submit_appointment()
        data = page.read_appointment_data(case)
        fields_to_check = [
            ('facility', 'get_booked_facility'),
            ('hospital_readmission', 'get_booked_hosp_readmission'),
            ('healthcare_program', 'get_booked_program'),
            ('visit_date', 'get_booked_visit_date'),
            ('comment', 'get_booked_comment')
        ]
        for field, method in fields_to_check:
            actual_value = getattr(page, method)()
            expected_value = data[field]
            assert actual_value == expected_value, \
                f"{field} mismatch. Expected '{expected_value}', but got '{actual_value}'"

    def test_appointment_negative(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('empty date field')
        page.submit_appointment()
        expected_error_messages = ["Заповніть це поле.", "Please fill out this field.", "Заполните это поле."]
        error_msg = page.get_date_error_msg()
        assert error_msg in expected_error_messages, f"Expected one of {expected_error_messages}, but got '{error_msg}'"
        expected_url = page.URL
        current_url = self.driver.current_url
        assert expected_url == current_url, f"Expected URL '{expected_url}', but got '{self.driver.current_url}'"
