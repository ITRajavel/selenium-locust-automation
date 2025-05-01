import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Pytest fixture to set up and tear down WebDriver
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_login_logout(driver):
    """Test login and logout functionality on the Saucedemo page"""
    driver.get("https://www.saucedemo.com/")

    # Wait and log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for product page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Open menu and logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    
    
