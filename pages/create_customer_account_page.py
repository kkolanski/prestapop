from pages.base_page import BasePage
from utils.gender import Gender
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateCustomerAccountPageLocators:
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    LAST_NAME_INPUT = (By.ID, "customer_lastname")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    BIRTH_DAY = (By.ID, "days")
    BIRTH_MONTH = (By.ID, "months")
    BIRTH_YEAR = (By.ID, "years")

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

    def select_birthdate(self, day, month, year):
        """
        Selects user birthdate (day month and year)
        """
        # Wybór dnia
        birth_day_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_DAY))
        birth_day_select.select_by_value(day)
        # Wybór miesiąca
        birth_month_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_MONTH))
        birth_month_select.select_by_value(month)
        # Wybór roku
        birth_year_select = Select(self.driver.find_element(*CreateCustomerAccountPageLocators.BIRTH_YEAR))
        birth_year_select.select_by_value(year)

    def get_email(self):
        """
        Gets email visible in the Email input
        """
        # Odszukać to pole
        el = self.driver.find_element(*CreateCustomerAccountPageLocators.EMAIL_INPUT)
        # Pobrać tekst i zwrócić go
        return el.get_attribute("value")

