import traceback

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ROC.ROCTasks.Login import Login
from ROC.ROCTasks.Logout import Logout
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://roc.robi.com.bd/ROC/ROCPages/Pages/ROBIROC_Login.aspx")
driver.maximize_window()
login = Login(driver)

login.insertUsername()
login.insertPassword()
login.clickSignin()
login.isUserLoggedIn()
print("Home Page available:", login.isHomePage())
print("ROC Controller available: ", login.isRocControllerTextAvailable())
logout = Logout(login.driver)
logout.logout()

driver.close()

driver.quit()
