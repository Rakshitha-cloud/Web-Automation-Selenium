import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ------------------------------
# Fixture: WebDriver Setup
# ------------------------------


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()

# ------------------------------
# Add metadata to pytest-html report (new way)
# ------------------------------


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata.clear()  # Clear default metadata if any


def pytest_html_report_title(report):
    report.title = "Web Automation Project Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project: Web Automation Project"])
    prefix.extend([f"Tester: Rakshitha N"])
    prefix.extend([f"Browser: Chrome"])
    prefix.extend([f"Framework: Pytest + Selenium"])
