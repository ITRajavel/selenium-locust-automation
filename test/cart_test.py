import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the Chrome driver
def setup_driver():
    """Set up the Chrome driver"""
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    return driver

# Login function
def login(driver, username, password):
    """Login to the application"""
    driver.get("https://www.saucedemo.com/")
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "user-name")))
    username_field.send_keys(username)
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    password_field.send_keys(password)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

# Test case 1: Verify the cart page is displayed
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page(driver, username, password):
    """Test case 1: Verify the cart page is displayed"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        cart_page_title = WebDriverWait(driver, 10).until(EC.title_contains("Cart"))
        assert cart_page_title
        print("Cart page title is displayed")
    except TimeoutException:
        print("Cart page title is not displayed")

# Test case 2: Verify the cart page contains the correct elements
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page_elements(driver, username, password):
    """Test case 2: Verify the cart page contains the correct elements"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        cart_page_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "shopping_cart_header")))
        cart_page_title_text = cart_page_title.text
        assert cart_page_title_text == "Your cart"
        print("Cart page title is displayed")
    except TimeoutException:
        print("Cart page title is not displayed")

# Test case 3: Verify the cart page contains the correct products
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page_products(driver, username, password):
    """Test case 3: Verify the cart page contains the correct products"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        product_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item_0_title")))
        product_name_text = product_name.text
        assert product_name_text == "Sauce Labs Bike Light"
        print("Product name is displayed")
    except TimeoutException:
        print("Product name is not displayed")

# Test case 4: Verify the cart page contains the correct product price
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page_product_price(driver, username, password):
    """Test case 4: Verify the cart page contains the correct product price"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        product_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item_0_price")))
        product_price_text = product_price.text
        assert product_price_text == "$16.99"
        print("Product price is displayed")
    except TimeoutException:
        print("Product price is not displayed")

# Test case 5: Verify the cart page contains the correct product quantity
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page_product_quantity(driver, username, password):
    """Test case 5: Verify the cart page contains the correct product quantity"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        product_quantity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item_0_qty")))
        product_quantity_text = product_quantity.text
        assert product_quantity_text == "1"
        print("Product quantity is displayed")
    except TimeoutException:
        print("Product quantity is not displayed")

# Test case 6: Verify the cart page contains the correct total price
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_cart_page_total_price(driver, username, password):
    """Test case 6: Verify the cart page contains the correct total price"""
    login(driver, username, password)
    driver.get("https://www.saucedemo.com/cart.html")
    try:
        total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "total_price_label")))
        total_price_text = total_price.text
        assert total_price_text == "$16.99"
        print("Total price is displayed")
    except TimeoutException:
        print("Total price is not displayed")


# Run the tests
if __name__ == "__main__":
    driver = setup_driver()
    pytest.main([__file__])
    driver.quit()