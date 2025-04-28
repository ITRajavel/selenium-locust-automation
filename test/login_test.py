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

def test_add_to_cart(driver):
    """Test adding an item to the cart"""
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Login to the application
    test_login(driver)

    # Find the first item on the page
    item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

    # Add the item to the cart
    item.click()

    # Verify the item was added to the cart
    assert driver.find_element(By.ID, "shopping_cart_container").is_displayed()

def test_remove_from_cart(driver):
    """Test removing an item from the cart"""
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Login to the application
    test_login(driver)

    # Add an item to the cart
    test_add_to_cart(driver)

    # Find the cart icon
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
    )

    # Click the cart icon
    cart_icon.click()

    # Find the remove button
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )

    # Click the remove button
    remove_button.click()


def test_checkout(driver):
    """Test the checkout process"""
    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")

    # Login to the application
    test_login(driver)

    # Add an item to the cart
    test_add_to_cart(driver)

    # Click the cart icon
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
    )
    cart_icon.click()

    # Click the checkout button
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

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

    # Click the continue button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()

    # Verify the checkout was successful
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"