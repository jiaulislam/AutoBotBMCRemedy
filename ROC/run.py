# from ROC.Locators.HomePage import HomePage
from ROC.Locators.Locator import Locator

# driver = HomePage("Jibon")
driver = Locator("Jibon")

print(driver.get_value())
print(driver)
