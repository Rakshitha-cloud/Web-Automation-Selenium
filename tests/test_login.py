import pytest
from pages.login_page import LoginPage
import time

# test function


def test_invalid_login(driver):
    # Create page object
    login_page = LoginPage(driver)

    # Go to login page
    # Replace with your real URL
    login_page.go_to(
        "file:///C:/Users/Lenovo/OneDrive%20-%20MSFT/Desktop/my_demo_website/index.html")

    # Attempt login with invalid credentials
    login_page.login("wronguser", "wrongpass")

    # Assert error message appears
    assert login_page.get_error() == "Invalid credentials!"

# Pause to see the browser
    time.sleep(10)


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to(
        "file:///C:/Users/Lenovo/OneDrive%20-%20MSFT/Desktop/my_demo_website/index.html")
    login_page.login("admin", "admin123")
    alert_text = driver.switch_to.alert.text
    assert "Login successful!" in alert_text
    driver.switch_to.alert.accept()

 # Pause to see the browser
    time.sleep(10)


# input("Press Enter to close the browser...")
