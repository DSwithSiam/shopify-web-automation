from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "account_email")  # নিশ্চিত করুন সঠিক ID
        self.continue_button = (By.XPATH, "//button[@type='submit']")
        self.password_field = (By.ID, "account_password")  # নিশ্চিত করুন সঠিক ID
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_title = "Dashboard"

    def enter_email(self, email):
        """ইমেল ফিল্ডে ইমেল এন্টার করুন"""
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.email_field)).send_keys(email)

    def continue_with_email(self):
        """Continue বাটনে ক্লিক করুন"""
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.continue_button)).click()

    def enter_password(self, password):
        """পাসওয়ার্ড ফিল্ডে পাসওয়ার্ড এন্টার করুন"""
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        """লগইন বাটনে ক্লিক করুন"""
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.login_button)).click()

    
