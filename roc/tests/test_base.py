import unittest

from selenium import webdriver
from utilites.static_data import ROCData
from webdriver_manager.chrome import ChromeDriverManager


class TestBase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get(ROCData.ROC_URL)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        del cls


if __name__ == '__main__':
    unittest.main()
