from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extract_all_elements(url, driver_path, username=None, password=None):
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.get(url)

    # Optional login
    if username and password:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
            time.sleep(2)
            username_field = driver.find_element(By.XPATH, "//input[@type='text' or contains(@name,'user')]")
            password_field = driver.find_element(By.XPATH, "//input[@type='password']")
            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            time.sleep(3)
        except Exception as e:
            print(f"Login failed: {e}")

    # Wait for page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def extract_info(el):
        return {
            "tag": el.tag_name,
            "type": el.get_attribute("type") or el.tag_name,
            "name": el.get_attribute("name") or "",
            "id": el.get_attribute("id") or "",
            "class": el.get_attribute("class") or "",
            "placeholder": el.get_attribute("placeholder") or "",
            "value": el.get_attribute("value") or "",
            "text": el.text.strip()
        }

    tags_to_extract = [
    "input", "textarea", "select", "button", "a", "div", "span", "label",
    "img", "h1", "h2", "h3", "h4", "h5", "h6",  # Headings
    "p", "ul", "ol", "li",                    # Paragraph and lists
    "table", "thead", "tbody", "tr", "td", "th",  # Table elements
    "form", "iframe", "video", "audio", "nav", "footer", "header"
]
    elements = []

    for tag in tags_to_extract:
        found_elements = driver.find_elements(By.TAG_NAME, tag)
        for el in found_elements:
            elements.append(extract_info(el))

    driver.quit()
    return elements
