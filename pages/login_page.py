# pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME = (By.ID, "username")   # Replace with your website's element ID
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    ERROR_MSG = (By.ID, "errorMsg")

    # Navigate to login page
    def go_to(self, url):
        self.driver.get(url)

    # Login action
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    # Get error message
    def get_error(self):
        return self.find(self.ERROR_MSG).text
