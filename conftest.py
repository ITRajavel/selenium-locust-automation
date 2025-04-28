import pytest
from selenium import webdriver

# Set up Chrome driver
@pytest.fixture(scope="session")
def driver():
    """Set up Chrome driver for testing"""
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()