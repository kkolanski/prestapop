from pages.base_page import BasePage
from utils.gender import Gender
from selenium.webdriver.common.by import By

class CreateCustomerAccountPageLocators:
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")

class CreateCustomerAccountPage(BasePage):
    def choose_gender(self, gender):
        """
        Chooses gender
        """
        if gender == Gender.FEMALE:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_FEMALE).click()
        else:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_MALE).click()

    def enter_last_name(self, last_name):
        """
        Enters last name
        """
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.LAST_NAME_INPUT)
        el.send_keys(last_name)

    def enter_password(self, password):
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.PASSWORD_INPUT)
        el.send_keys(password)

    def get_email(self):
        """
        Gets email visible in the Email input
        """
        # Odszukać to pole
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.EMAIL_INPUT)
        # Pobrać tekst i zwrócić go
        return el.get_attribute("value")

