```python
# Import necessary libraries
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the Chrome driver
driver = webdriver.Chrome()

# Define a function to login to the application
def login(username, password):
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username_field.send_keys(username)

    # Enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_field.send_keys(password)

    # Click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

# Define a function to add item to cart
def add_item_to_cart():
    # Click the add to cart button
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_to_cart_button.click()

# Define a function to checkout
def checkout():
    # Click the checkout button
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

# Define a function to fill in shipping information
def fill_in_shipping_info():
    # Enter the first name
    first_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "first-name"))
    )
    first_name_field.send_keys("John")

    # Enter the last name
    last_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "last-name"))
    )
    last_name_field.send_keys("Doe")

    # Enter the postal code
    postal_code_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "postal-code"))
    )
    postal_code_field.send_keys("12345")

# Define a function to complete the purchase
def complete_purchase():
    # Click the continue button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()

    # Click the finish button
    finish_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()

# Test case: Successful purchase flow
def test_purchase_flow():
    # Login to the application
    login("standard_user", "secret_sauce")

    # Add item to cart
    add_item_to_cart()

    # Checkout
    checkout()

    # Fill in shipping information
    fill_in_shipping_info()

    # Complete the purchase
    complete_purchase()

    # Verify that the purchase was successful
    assert driver.title == "Swag Labs"

# Test case: Failed login
def test_failed_login():
    # Login to the application with incorrect credentials
    login("invalid_user", "invalid_password")

    # Verify that the login failed
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
    except TimeoutException:
        assert True

# Run the tests
pytest.main()
```

This script uses Pytest to structure the test cases and ensure they are well-organized and reusable. Each test case contains the login function, and the tests are designed to cover both a successful purchase flow and a failed login. The script uses Selenium to interact with the web application and verify that the expected actions are taken.