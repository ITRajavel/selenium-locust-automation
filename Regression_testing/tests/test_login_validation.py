import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the test environment
@pytest.fixture
def driver():
    """Initialize the Chrome driver"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    """Test the login functionality"""
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Find the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )

    # Enter the username
    username_field.send_keys("standard_user")

    # Find the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Enter the password
    password_field.send_keys("secret_sauce")

    # Find the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Click the login button
    login_button.click()

    # Verify the login was successful
    assert driver.title == "Swag Labs"

def test_invalid_Password(driver):
    """Test the login functionality"""
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Find the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )

    # Enter the username
    username_field.send_keys("standard_user")

    # Find the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Enter the password
    password_field.send_keys("secret")

    # Find the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Click the login button
    login_button.click()

    # Verify the login was successful
    assert driver.current_url =="https://www.saucedemo.com/inventory.html"


def test_Empty_Field(driver):
   
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Find the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )

    # Enter the username
    username_field.send_keys(" ")

    # Find the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Enter the password
    password_field.send_keys(" ")

    # Find the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Click the login button
    login_button.click()


    # Verify the login was successful
    assert driver.current_url =="https://www.saucedemo.com/inventory.html"

def test_Invalid_Username(driver):
   
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Find the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )

    # Enter the username
    username_field.send_keys(" ")

    # Find the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    # Enter the password
    password_field.send_keys(" ")

    # Find the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    # Click the login button
    login_button.click()

    # Verify the login was successful
    assert driver.current_url =="https://www.saucedemo.com/inventory.html"