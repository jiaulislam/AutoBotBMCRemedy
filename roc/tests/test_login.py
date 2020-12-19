from ..job.login_job import LoginJob
from ..job.logout_job import LogoutJob
from roc.tests.test_base import TestBase


class TestLogin(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_roc_login(self):
        self.login = LoginJob(self.driver)
        self.logout = LogoutJob(self.driver)
        self.assertEqual(self.login.roc_login(), True)
        self.logout.roc_logout()

