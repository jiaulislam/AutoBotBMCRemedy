from ROC.Locators.HomePage import HomePage
# from ROC.Locators.BaseLocator import BaseLocator

driver = HomePage("Jibon")
# driver = BaseLocator("Ribbon")

print(driver.get_value())
print(driver)
