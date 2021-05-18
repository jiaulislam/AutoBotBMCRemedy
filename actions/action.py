from combiners.cancel import Cancel
from combiners.close import Close
from combiners.create import Create
from combiners.ldmaworker import Parser
from drivers.chrome import ChromeBrowser


class CreateNewChangeRequest(ChromeBrowser, Create):
    """ A Sub-Class of Handler and CreateChangeRequest module to create new Change Requests """

    __createChangeRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def createRequest(self):
        """ Call all the functions from CreateChangeRequest to create change requests """
        self.get_bmc_website()
        self.__createChangeRequest = Create(self.browser)
        self.__createChangeRequest.createNCR()


class CloseChangeRequest(ChromeBrowser, Close):
    """ A Sub-Class of Handler and CloseChangeRequest module to close Change Requests """

    __closeMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def closeRequest(self):
        """ Call all the functions from CloseChangeRequests to close change requests """
        self.get_bmc_website()
        self.__closeMyRequest = Close(self.browser)
        self.__closeMyRequest.closeRequest()


class CancelChangeRequests(ChromeBrowser, Cancel):
    """ A Sub-Class of Handler and CancelChangeRequest module to Cancel Change Requests """

    __cancelMyRequest = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def cancelRequests(self):
        """ Call all the functions from CancelChangeRequests to cancel change requests """
        self.get_bmc_website()
        self.__cancelMyRequest = Cancel(self.browser)
        self.__cancelMyRequest.cancelRequest()


class ParserLDMA(ChromeBrowser, Parser):
    __parser = None

    @classmethod
    def setUpDriver(cls):
        super().setUpDriver()

    def parseLDMA(self, link_ids: list[str] = None, site_ids: list[str] = None):
        self.get_ldma_website()
        self.__parser = Parser(self.browser)
        self.__parser.parseLinkBudget(link_ids, site_ids)
