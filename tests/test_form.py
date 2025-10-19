import pytest
import time
from pages.form_page import FormPage


def test_form_submission(driver):
    form_page = FormPage(driver)

    # Open your local form page
    form_page.go_to(
        "file:///C:/Users/Lenovo/OneDrive%20-%20MSFT/Desktop/my_demo_website/form.html")

    # Fill form details
    form_page.fill_form(
        name="Rakshitha N",
        email="rakshitha@example.com",
        message="This is a test message.",
        country="India"
    )

    # Submit form
    form_page.submit()

    # Wait for alert and validate
    time.sleep(1)
    alert_text = driver.switch_to.alert.text
    assert "Form submitted successfully!" in alert_text
    driver.switch_to.alert.accept()

    # Verify message below form
    success_message = form_page.get_success_message()
    assert "Thanks for contacting us!" in success_message

    # Pause to view browser
    time.sleep(10)
