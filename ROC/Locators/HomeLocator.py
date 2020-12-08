from ROC.Locators.Locator import Locator


class HomeLocator(Locator):

    ROC_CONTROLLER_TEXT = "//span[contains(text(), 'Rollout Controller')]"
    LOGOUT_IMG_BTN = "//a//img[1]"
    LOGOUT_BTN = "//input[@id='ctl00_Button1']"

