import pytest

from profile.pages.page_appointment import PageAppointment


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestAppointment:

    def test_make_appointment(self):
        page = PageAppointment(self.driver)
        page.select_facility('Seoul CURA Healthcare Center')
        page.check_hospital_readmission()
        page.check_healthcare_program('None')
        pass

    def test_appointment_min(self):
        pass

    def test_appointment_negative(self):
        pass
