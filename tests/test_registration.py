
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://accounts.shopify.com/signup")
    
    yield driver
    driver.quit()

def test_registration(setup):
    registration_page = RegistrationPage(setup)
    registration_page.sign_up_with_email()
    registration_page.enter_email("testuser@example.com")
    registration_page.enter_first_name("masipul ")
    registration_page.enter_last_name("siam")
    registration_page.enter_password_1("StrongPassword123!")
    registration_page.enter_password_2("StrongPassword123!")
    registration_page.sign_up()


