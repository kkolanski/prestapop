from tests.base_test import BaseTest
from test_data.registration_data import RegistrationData
from utils.gender import Gender
from time import sleep

class RegistrationTest(BaseTest):
    """
    Registration tests
    """
    def test_no_name(self):
        """
        TC 001: User does not enter his name
        :return:
        """
        # KROKI
        # 1. Kliknij "Sign In"
        self.authentication_page = self.home_page.click_sign_in()
        # 2. Wpisz email
        # 3. Kliknij przycisk "Create account"
        self.create_customer_account_page = self.authentication_page.enter_email_and_click_create_account(RegistrationData.REGISTRATION_EMAIL)
        # 4. Wybierz płeć
        self.create_customer_account_page.choose_gender(Gender.FEMALE)
        # 5. Wpisz nazwisko
        self.create_customer_account_page.enter_last_name("Kowalski")
        # Sprawdź, czy email wpisany wcześniej wyświetla się polu email
        self.assertEqual(RegistrationData.REGISTRATION_EMAIL, self.create_customer_account_page.get_email())
        sleep(3)
