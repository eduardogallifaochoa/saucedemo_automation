import pytest
from selenium.webdriver.common.by import By
from utils.driver_setup import setup_driver

URL = "https://www.saucedemo.com/"

@pytest.fixture
def browser():
    driver = setup_driver()
    driver.get(URL)
    yield driver
    driver.quit()

def test_login_success(browser):
    """Valida el login exitoso con credenciales válidas."""
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    assert "inventory" in browser.current_url, "Login fallido"

def test_login_failure(browser):
    """Valida el mensaje de error al usar credenciales inválidas."""
    browser.find_element(By.ID, "user-name").send_keys("invalid_user")
    browser.find_element(By.ID, "password").send_keys("invalid_pass")
    browser.find_element(By.ID, "login-button").click()
    error_message = browser.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error_message, "Mensaje de error incorrecto"
