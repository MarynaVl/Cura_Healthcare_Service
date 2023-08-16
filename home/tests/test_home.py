import pytest

from home.pages.page_home import PageHome


@pytest.mark.usefixtures('chrome')
@pytest.mark.usefixtures('authentication')
class TestHome:

    def test_make_appointment_from_home_page(self):
        page = PageHome(self.driver)
        page.open_home()
        case = 'appointment with hospital readmission'
        page.set_appointment_data(case)
        page.submit_appointment()
        confirmation_msg = page.get_confirmation_msg()
        page.page_helper.assert_equal(confirmation_msg, 'Appointment Confirmation', 'Messages mismatch')
