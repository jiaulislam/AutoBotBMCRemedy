import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from utilites.static_data import BMCData, LDMAData


class ChromeDriver:
    """ A independent class for calling the browser WebDriver """
    browser: WebDriver = None

    @classmethod
    def setUpDriver(cls):
        options = Options()
        # options.headless = True # Run the Chrome driver in headless mode
        # options.add_argument("--disable-gpu") # It's recommended to turn of GPU while headless mode
        options.add_argument("--log-level=3")  # disable Info/Error/Warning in Chrome Driver
        options.add_experimental_option('excludeSwitches',
                                        ['enable-logging'])  # disable Dev Info info while running app
        options.add_argument("--start-maximized")  # start the chrome with maximized window
        os.environ['WDM_LOG_LEVEL'] = '0'  # Disable the logging of ChromeDriverManager()
        cls.browser: WebDriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    @classmethod
    def tearDownDriver(cls):
        cls.browser.quit()

    @classmethod
    def __del__(cls):
        del cls


class ChromeBrowser(ChromeDriver):
    """ A Sub-Class of Driver for additional functionalities.
        Example: Headless Mode, Session Handle, Cookies Handle, Open Links
    """

    def __init__(self):
        super().setUpDriver()

    def get_bmc_website(self):
        """ Get the BMC Remedy URL """
        self.browser.get(BMCData.BMC_URL)

    def get_ldma_website(self):
        """ Get the LDMA URL """
        self.browser.get(LDMAData.LDMA_URL)
