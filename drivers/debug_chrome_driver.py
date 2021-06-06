from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

BROWSER = "9999"  # set this to desired 4 digit port


def __remote_handler(port: str) -> Options:
    options = Options()
    options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    return options


def get_browser_window() -> WebDriver:
    return webdriver.Chrome(ChromeDriverManager().install(), options=__remote_handler(BROWSER))
