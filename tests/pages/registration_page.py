from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.XPATH, "//*[@id='account_email']")  
        self.first_name_field = (By.XPATH, "//*[@id='account_first_name']")  
        self.last_name_field = (By.XPATH, "//*[@id='account_last_name']")  
        self.password_field_1 = (By.XPATH, "//*[@id='account_password']")  
        self.password_field_2 = (By.XPATH, "//*[@id='password-confirmation']")  
        self.sign_up_with_email_button = (By.XPATH, "//*[@id='body-content']/div[2]/div/div[2]/div/div/div/div[3]/div/div[3]/a[1]")
        self.sign_up_button = (By.XPATH, "//*[@id='submit-disable']/button")

    def enter_email(self, email):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.email_field)
        ).send_keys(email)


    def enter_first_name(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        ).send_keys(email)


    def enter_last_name(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.last_name_field)
        ).send_keys(email)

    def enter_password_1(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field_1)
        ).send_keys(password)

    def enter_password_2(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field_2)
        ).send_keys(password)

    def sign_up_with_email(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_up_with_email_button)
        ).click()

    def sign_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_up_button)
        ).click()


    def is_registration_successful(self):
        return "Welcome" in self.driver.page_source  
