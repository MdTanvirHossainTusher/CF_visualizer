from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from browser.browser_factory import chrome_driver
import json
import os

config_path = os.path.join(os.path.dirname(__file__), "../resources/config_data.json")


def get_web_url():
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
    return config_data["url"]


def create_driver():
    options = chrome_driver()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(get_web_url())
    return driver


driver = create_driver()
