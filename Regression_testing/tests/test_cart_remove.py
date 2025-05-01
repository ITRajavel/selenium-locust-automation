import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Setup the Chrome driver"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_remove_product_from_cart(driver):
   
    driver.get("https://www.saucedemo.com/")

    login(driver)


def login(driver):

    username_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username_input.send_keys("standard_user")

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_input.send_keys("secret_sauce")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    product.click()

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
    )
    cart_button.click()

    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    )
    remove_button.click()

    assert driver.find_element(By.ID, "cart_contents_container").text != ""


if __name__ == "__main__":
    pytest.main()