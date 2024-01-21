from pages.base_page import BasePage
from utils.gender import Gender
from selenium.webdriver.common.by import By

class CreateCustomerAccountPageLocators:
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")

class CreateCustomerAccountPage(BasePage):
    def choose_gender(self, gender):
        if gender == Gender.FEMALE:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_FEMALE).click()
        else:
            self.driver.find_element(*CreateCustomerAccountPageLocators.GENDER_MALE).click()
