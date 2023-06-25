from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from browser.browser_factory import chrome_driver
import utils.load_json_file as load_file
import os

config_data_file_path = os.path.join(
    os.path.dirname(__file__), "../resources/config_data.json"
)


def create_driver():
    options = chrome_driver()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(load_file.get_web_url(config_data_file_path, "url"))
    return driver


driver = create_driver()
