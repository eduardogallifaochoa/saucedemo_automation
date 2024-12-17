from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver():
    """Configura y devuelve el navegador Chrome."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Abre Chrome maximizado
    chrome_options.add_argument("--disable-extensions")  # Deshabilita extensiones
    service = Service()  # Configuración de servicio
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
