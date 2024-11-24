
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))



import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.shopify.com/login")
    yield driver
    driver.quit()

def test_login_valid(setup):
    login_page = LoginPage(setup)
    login_page.enter_email("swadeshikunjo@gmail.com")
    login_page.continue_with_email()
    login_page.enter_password("dc%EW$eNBe8k)Q/")
    login_page.click_login()

