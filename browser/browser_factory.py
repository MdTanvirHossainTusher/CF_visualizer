from selenium.webdriver.chrome.options import Options


def chrome_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options
