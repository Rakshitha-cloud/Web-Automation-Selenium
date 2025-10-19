from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "name")
        self.email_input = (By.ID, "email")
        self.message_input = (By.ID, "message")
        self.country_dropdown = (By.ID, "country")
        self.submit_button = (By.ID, "submitBtn")
        self.success_msg = (By.ID, "successMsg")

    def go_to(self, url):
        self.driver.get(url)

    def fill_form(self, name, email, message, country):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.message_input).send_keys(message)
        self.driver.find_element(*self.country_dropdown).send_keys(country)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text
