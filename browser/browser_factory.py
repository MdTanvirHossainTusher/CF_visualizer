from selenium.webdriver.chrome.options import Options
import utils.load_json_file as load_file
import os

config_data_file_path = os.path.join(
    os.path.dirname(__file__), "../resources/config_data.json"
)


def chrome_driver():
    options = Options()
    options.add_argument(load_file.get_web_url(config_data_file_path, "browser_mode"))
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options
