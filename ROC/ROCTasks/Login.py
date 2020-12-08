from ROC.Locators.LoginLocator import LoginLocator as LL
from Pages.base import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def insertUsername(self):
        self.write(LL.get_by_Xpath(LL.USERNAME_INPUT), 'masud.utsp')

    def insertPassword(self):
        self.write(LL.get_by_Xpath(LL.PASSWORD_INPUT), 'Masud012345')

    def clickSignin(self):
        self.click(LL.get_by_Xpath(LL.SIGN_IN_BTN))

    def isAlreadyLoggedIn(self):
        pass

    def 
