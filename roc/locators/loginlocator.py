from roc.locators.locator import Locator


class LoginLocator(Locator):

    USERNAME_INPUT = "//input[@id='txtUsername']"
    PASSWORD_INPUT = "//input[@id='txtPassword']"
    SIGN_IN_BTN = "//input[@id='btnLogin']"
