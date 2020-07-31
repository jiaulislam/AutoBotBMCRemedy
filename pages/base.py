from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

''' 
The BasePage class is a base class that all the Pages that will inherit from this
BasePage class. Some most common method is written here that we're gonna need 
all over the project/pages to work with.
'''


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator) -> object:
        """ Find the element by the help of the locator that user shared """
        return self.driver.find_element(*locator)

    def find_elements(self, *locator) -> object:
        """ Find the elements by the help of the locator that user shared """
        return self.driver.find_elements(*locator)

    def is_visible(self, by_locator) -> bool:
        """ If the element is found in the Page then return True else False """
        element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def click(self, by_locator) -> None:
        """ Click a web element by a locator shared by the user """
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).click()
        except ElementClickInterceptedException:
            button = WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(by_locator))
            button.click()

    def write(self, by_locator, text) -> None:
        """ Write the text in web element by a locator shared by the user """
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def hover_over(self, by_locator) -> None:
        """ Hover over the element shared by the user locator """
        element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_to_frame(self, by_locator) -> None:
        """ Switch to a frame by a frame locator """
        user_frame = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
        self.driver.switch_to.frame(user_frame)

    def double_click(self, by_locator) -> None:
        """ Double click on a element by a locator """
        element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator))
        ActionChains(self.driver).double_click(element).perform()

    def switch_to_window(self):
        """ Dynamic wait for a new window to open """
        handles = self.driver.window_handles
        return WebDriverWait(self.driver, self.timeout).until(ec.new_window_is_opened(handles))

    def send_ctrl_plus_a(self, by_locator):
        """ Sends CTRL + A action to a page """
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(by_locator)).click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    def get_value_of_element(self, by_locator):
        """ Get the text value of a web element shared by a user """
        val_of_elem = WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(by_locator)).get_attribute("value")
        return val_of_elem

    def check_for_expected_frame(self, by_locator) -> None:
        """ Checks for expected frames and press OK button in the frame """
        try:
            self.switch_to_frame(by_locator)
            self.click(by_locator)
            self.driver.switch_to.default_content()
        except NoSuchFrameException:
            pass

    def back_to_home_page(self, by_locator):
        """ Return to the homepage """
        try:
            self.click(by_locator)
        except NoSuchElementException:
            self.click(by_locator)
