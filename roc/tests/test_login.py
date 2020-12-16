from ..job.login_job import LoginJob
from roc.tests.test_base import TestBase


class TestLogin(TestBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_roc_login(self):
        self.login = LoginJob(self.driver)
        self.assertEqual(self.login.roc_login(), True)
