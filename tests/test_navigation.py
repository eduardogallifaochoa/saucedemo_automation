import pytest
from selenium.webdriver.common.by import By
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

def test_menu_button(browser):
    """Valida que el botón de menú se abre correctamente."""
    browser.find_element(By.ID, "react-burger-menu-btn").click()
    menu_visible = browser.find_element(By.CLASS_NAME, "bm-menu").is_displayed()
    assert menu_visible, "El menú no se abrió correctamente"
