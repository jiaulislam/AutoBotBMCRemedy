from roc.roctasks.logout import Logout


class LogoutJob(Logout):

    def __init__(self, driver):
        super().__init__(driver)
        self.logout = Logout(self.driver)

    def roc_logout(self):
        self.logout.logout()