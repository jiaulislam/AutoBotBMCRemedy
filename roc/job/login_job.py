from roc.roctasks.login import Login


class LoginJob(Login):

    def __init__(self, driver):
        super().__init__(driver)
        self.login = Login(self.driver)
        self.login.set_username()
        self.login.set_password()

    def roc_login(self):
        self.login.insertUsername()
        self.login.insertPassword()
        self.login.clickSignin()
        self.login.isUserLoggedIn()
        return self.login.isHomePage()
