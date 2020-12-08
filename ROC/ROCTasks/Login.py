import sys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ROC.Locators.HomeLocator import HomeLocator
from ROC.Locators.LoginLocator import LoginLocator as LL
from Pages.base import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__USER_ALREADY_LOGGED_IN_ALERT = "Do you want to terminate the previous session or not?  " \
                                              "Please click on  OK  to terminate the previous session otherwise " \
                                              "click on Cancel to continue the previous session."
        self.__INVALID_CREDENTIALS = "User name or password missmatch...."
        self.__ROC_CONTROLLER_JS_INJECTION = "document.getElementsByTagName(\"span\")[0]"

    def insertUsername(self) -> None:
        self.write(LL.get_by_Xpath(LL.USERNAME_INPUT), 'masud.utsp')

    def insertPassword(self) -> None:
        self.write(LL.get_by_Xpath(LL.PASSWORD_INPUT), 'Masud012345')

    def clickSignin(self) -> None:
        self.click(LL.get_by_Xpath(LL.SIGN_IN_BTN))

    def isUserLoggedIn(self) -> bool:

        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alertBox = self.driver.switch_to.alert
            text_of_alert = alertBox.text

            if text_of_alert == self.__USER_ALREADY_LOGGED_IN_ALERT:
                choice: str = input("Enter 'Y' to Proceed or 'N' to Cancel --> ")
                while True:
                    if choice.lower() == 'y':
                        alertBox.accept()
                        break
                    elif choice.lower() == 'n':
                        alertBox.dismiss()
                        self.driver.quit()
                        sys.exit()
                    else:
                        choice = input("invalid input ! Try Again >>> ")
            elif text_of_alert == self.__INVALID_CREDENTIALS:
                self.driver.quit()
                print("Invalid Credentials used. Please try later.")
                sys.exit()
            else:
                print("Something Happening")
        except TimeoutException:
            if self.isHomePage():
                return True

    def isRocControllerTextAvailable(self):

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            LL.get_by_Xpath(HomeLocator.ROC_CONTROLLER_TEXT))).text

        if element == "Rollout Controller":
            return True
        else:
            return False

    def isHomePage(self) -> bool:

        try:
            return WebDriverWait(self.driver, 10).until(EC.title_is("HOME:"))
        except TimeoutException as e:
            raise Exception(e)
