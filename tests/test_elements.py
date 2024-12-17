from selenium.webdriver.common.by import By
import pytest
from utils.driver_setup import setup_driver

URL = "https://www.saucedemo.com/"

@pytest.fixture
def browser():
    driver = setup_driver()
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()

def test_product_title(browser):
    """Verifica que el título de productos sea correcto."""
    product_title = browser.find_element(By.CLASS_NAME, "title").text
    assert product_title == "Products", "El título del producto es incorrecto"
