from utils.gender import Gender
from faker import Faker
import random


class RegistrationData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.registration_first_name = fake.first_name()
        self.registration_last_name = fake.last_name()
        self.registration_email = fake.email()
        self.registration_gender = random.choice([Gender.FEMALE, Gender.MALE])
        data = fake.date_of_birth()
        self.day_of_birth = str(data.day)
        self.month_of_birth = str(data.month)
        self.year_of_birth = str(data.year)
        self.password = fake.password()