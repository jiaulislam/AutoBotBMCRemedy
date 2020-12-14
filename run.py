from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from roc.roctasks.login import Login
from roc.roctasks.logout import Logout
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://roc.robi.com.bd/ROC/ROCPages/Pages/ROBIROC_Login.aspx")
driver.maximize_window()
login = Login(driver)

login.set_username()
login.set_password()

login.insertUsername()
login.insertPassword()
login.clickSignin()
login.isUserLoggedIn()
print("Home Page available:", login.isHomePage())
print("roc Controller available: ", login.isRocControllerTextAvailable())
logout = Logout(login.driver)
logout.logout()

driver.close()

driver.quit()
