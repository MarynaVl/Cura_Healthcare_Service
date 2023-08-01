import pytest

from profile.pages.page_appointment import PageAppointment


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestAppointment:

    def test_make_appointment(self):
        page = PageAppointment(self.driver)
        page.set_appointment_data('appointment without hospital readmission')
        page.submit_appointment()
        # дописати assert

    def test_appointment_min(self):
        pass

    def test_appointment_negative(self):
        pass
