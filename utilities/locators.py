from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """ Login Page related XPATH class Variable are declared here """
    # ==> LOGIN PAGE LOCATORS <== #
    LOGO_IMG = (By.XPATH, "//img[@src='images/login_logo.gif']")
    USERNAME_TEXTBOX = (By.XPATH, "//*[@id='username-id']")
    PASSWORD_TEXTBOX = (By.XPATH, "//*[@id='pwd-id']")
    LOGIN_BUTTON = (By.XPATH, "//input[@name='login']")


class PageLocators(object):
    # ==> HOME PAGE LOCATORS <== #
    IT_HOME_TEXT = (By.XPATH, "//label[@id='label80137'][contains(text(), 'IT Home')]")
    APPLICATION_BUTTON = (By.XPATH, "//*[@id='reg_img_304316340']")
    CHANGE_MANAGEMENT_LIST = (By.XPATH, "//*[text()='Change Management']")
    NEW_CHANGE_LIST = (By.XPATH, "//*[text()='New Change']")
    HOME_ICON_BTN = (By.ID, "reg_img_304248660")

    # ==> NEW_CHANGE PAGE LOCATORS <== #
    SUMMARY_TEXTBOX = (By.XPATH, "//*[@id='arid_WIN_3_1000000000']")
    NOTES_TEXTBOX = (By.XPATH, "//*[@id='arid_WIN_3_1000000151']")
    MANAGER_GROUP_BTN = (By.XPATH, "//div[@id='WIN_3_1000000015']//a[@class='btn btn3d menu']")
    IMPLEMENTATION_MENU = (
        By.XPATH, "//div[@class='MenuOuter']//div[@class='MenuTableContainer']//table[@class='MenuTable']"
                  "//tbody[@class='MenuTableBody']//tr[@class='MenuTableRow']//td[@class='MenuEntryName']"
                  "[contains(text(),'Implementation')]")

    # ------------------ CHANGE_MANAGER_DEPARTMENT ------------------------------ #
    TNR_GROUP_MENU = (By.XPATH, "//td[contains(text(),'Transport Network Rollout')]")
    ANR_GROUP_MENU = (By.XPATH, "//td[contains(text(),'Access Network Rollout')]")

    # ------------------ CHANGE_MANAGER_TECHNOLOGY DIVISION ----------------------- #
    TX_OPTIMIZATION_SELECT_BTN = (By.XPATH, "//td[contains(text(),'Tx Optimization and Modernization')]")
    RADIO_ROLLOUT_SELECT_BTN = (By.XPATH, "//td[contains(text(),'Radio Rollout')]")

    CHANGE_MANAGER_MENU_BTN = (By.XPATH, "//*[@id='WIN_3_1000000403']/a")

    #  ----------------- NAMES OF THE CHANGE MANAGERS --------------------------- #
    CHANGE_MANAGER_SHAHED = (By.XPATH, "//div[@class='MenuOuter']//*[text()='Muhammad Shahed']")
    CHANGE_MANAGER_RIPAN = (By.XPATH, "//div[@class='MenuOuter']//*[text()='Ripan Kumar']")
    CHANGE_MANAGER_FUAD = (By.XPATH, "//div[@class='MenuOuter']//*[text()='Faisal Mahmud Fuad']")
    CHANGE_MANAGER_MUSFIQ = (By.XPATH, "//div[@class='MenuOuter']//*[text()= 'Md. Musfiqur  Rahman'']")
    CHANGE_MANAGER_SHAHRIAR = (By.XPATH, "//div[@class='MenuOuter']//*[text()='Shahriar Mahbub']")
    CHANGE_MANAGER_SUMON = (By.XPATH, "//div[@class='MenuOuter']//*[text()='Sumon Kumar Biswas']")

    # ==> LOCATION SUB-PAGE LOCATORS <== #
    LOCATION_MENU_BTN = (By.XPATH, "//img[@id='reg_img_303935000']")
    CLEAR_BUTTON = (By.XPATH, "//*[@id='WIN_0_303915400']/div/div")
    SEARCH_ICON_IMG = (By.XPATH, "//img[@id='reg_img_304249820']")
    COMPANY_TEXTBOX = (By.XPATH, "//textarea[@id='arid_WIN_0_1000000001']")
    REGION_TEXTBOX = (By.XPATH, "//textarea[@id='arid_WIN_0_200000012']")
    SITE_GROUP_TEXTBOX = (By.XPATH, "//textarea[@id='arid_WIN_0_200000007']")
    SITE_TEXTBOX = (By.XPATH, "//textarea[@id='arid_WIN_0_260000001']")
    SEARCH_LOCATION_BTN = (By.XPATH, "//div[@class='f1'][contains(text(),'Search')]")
    SELECT_LOCATION_BTN = (By.XPATH, "//div[contains(text(),'Select')]")
    OK_LOCATION_BTN = (By.XPATH, "//div[contains(text(),'OK')]")

    # ==> WORK_INFO NOTES & ATTACHMENT LOCATORS <== #
    INFO_NOTES_TEXTBOX = (By.XPATH, "//div[@id='WIN_3_304247080']//*[@id='arid_WIN_3_304247080']")
    ATTACH_FILE_ICON_BUTTON = (By.XPATH, "//img[@id='reg_img_304247100']")
    UPLOAD_ATTACHMENT_FRAME = (
        By.XPATH, "//iframe[@src='http://itsm-web.robi.com.bd:8080/arsys/resources/html/AttachmentPopup.html']")
    CHOOSE_ATTACHMENT_FRAME = (By.XPATH, "//input[@id='PopupAttInput']")
    OK_ATTACHMENT_FRAME_BUTTON = (By.XPATH, "//div[@id='PopupAttFooter']/a[contains(text(), 'OK')]")
    ADD_NOTE_ATTACHMENT_BUTTON = (By.XPATH, "//a[@id='WIN_3_304247110']//div[@class='f1'][contains(text(),'Add')]")
    MORE_DETAILS_BUTTON = (By.XPATH, "//div[@id='WIN_3_304247070']//a[@class='pagebtn ']")
    WORK_INFO_TYPE_BUTTON = (By.XPATH, "//input[@id='arid_WIN_3_304247210']")
    VIEW_ATTACHMENT_BUTTON = (By.ID, "reg_img_304252650")

    # ==> CHANGE CLASS TYPE SECTION LOCATORS <== #
    CHANGE_CLASS_TYPE_BUTTON = (By.XPATH, "//input[@id='arid_WIN_3_1000000568']")

    # ==> DATE PAGE LOCATORS <== #
    DATE_PAGE = (By.XPATH, "//a[contains(text(),'Date')]")
    START_DATE_INPUT = (By.XPATH, "//input[@id='arid_WIN_3_1000000350']")
    END_DATE_INPUT = (By.XPATH, "//input[@id='arid_WIN_3_1000000362']")

    # ==> TASK PAGE LOCATORS <== #
    TASK_PAGE = (By.XPATH, "//a[contains(text(),'Tasks')]")
    REQUEST_TYPE_BTN = (By.XPATH, "//input[@type='text' and @id='arid_WIN_3_10003042']")
    TASK_GROUP_TEMPLATE_BTN = (By.XPATH, "//td[contains(text(), 'Task Group Template')]")
    RELATE_BTN = (By.XPATH, "//div[contains(text(),'Relate')]")
    TASK_RELATE_BTN = (By.XPATH, "//*[@id='WIN_0_10006772']")
    TASK_GROUP_ROW_SPAN = (By.XPATH, "//span[contains(text(), 'Task Group')]")

    # ==> INITIATION TASK PAGE LOCATORS <== #
    INITIATION_TASK_SPAN = (By.XPATH, "//span[contains(text(), 'Initiation Phase Task (SOC)')]")

    # ==> DOWNTIME DURATION PAGE LOCATORS <== #
    SERVICE_DOWNTIME_DURATION_TASK_SPAN = (By.XPATH, "//span[contains(text(), 'Service Downtime Duration Task')]")

    # ==> SYSTEM  DOWNTIME TASK LOCATORS <== #
    SYSTEM_DOWNTIME_TASK = (By.XPATH, "//span[contains(text(), 'System Downtime Task')]")

    # ==> DOWNTIME WINDOW PAGE LOCATORS <== #
    SERVICE_DOWNTIME_WINDOW_TASK_SPAN = (By.XPATH, "//span[contains(text(), 'Service Downtime Window Task')]")

    # ==> REVIEW & CLOSE TASK PAGE LOCATORS <== #
    REVIEW_CLOSURE_TASK_SPAN = (By.XPATH, "//span[contains(text(), 'Review and Closure Task (SOC)')]")

    # FOR ALL THE 5 TASK COMMON PATH
    DATE_SECTOR_IN_TASK = (By.XPATH, "//a[contains(text(), 'Dates')]")
    START_TIME_IN_TASK = (By.XPATH, "//input[@id= 'arid_WIN_0_1000000350']")
    END_TIME_IN_TASK = (By.XPATH, "//input[@id= 'arid_WIN_0_1000000362']")
    SAVE_TASK_BTN = (By.XPATH, "//div[@class='f7'][contains(text(), 'Save')]")

    # ==> SAVE THE CHANGE REQUEST <== #
    SAVE_CHANGE_BTN = (By.XPATH, "//a[@id='WIN_3_1001']")

    # ==> IT-HOME BUTTON <== #
    IT_HOME_BUTTON = (By.XPATH, "//a[@class='btn'][contains(text(),'IT Home')]")

    # ==> FRAME OF CONFIRMATION <== #
    FRAME_OF_CONFIRMATION = (
        By.XPATH, "//iframe[@src='http://itsm-web.robi.com.bd:8080/arsys/resources/html/MessagePopup.html']")
    FRAME_OK_BUTTON = (By.XPATH, "//div[@id='PopupMsgFooter']//a[contains(text(),'OK')]")

    # ==> GET CHANGE NUMBER <== #
    CHANGE_NUMBER_VALUE = (By.XPATH, "//div[@id='WIN_3_1000000182']//textarea[@id='arid_WIN_3_1000000182']")

    # ==> LOGOUT PAGE LOCATORS <== #
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='f9'][contains(text(),'Logout')]")

    # ==> RELATIONSHIP PAGE LOCATORS <== #
    RELATIONSHIP_TAB = (By.XPATH, "//a[contains(text(), 'Relationships')]")
    RELATIONSHIP_TYPE_LIST = (By.XPATH, "//textarea[@id='arid_WIN_0_301541300']")
    CONFIGURATION_ITEM = (
        By.XPATH, "//tr[@class = 'MenuTableRow']//td[@class='MenuEntryName'][contains(text(), 'Configuration Item')]")
    RELATIONSHIP_TYPE_SELECT = (By.XPATH, "//td[@class='MenuEntryNameHover']")
    RELATIONSHIP_WINDOW_SEARCH_BTN = (
        By.XPATH, "//a[@id='WIN_0_10003600']//div[@class='f1'][contains(text(),'Search')]")
    RELATIONSHIP_ADVANCE_SEARCH_LINK = (By.XPATH, "//div[contains(text(),'Use Advanced Search')]")
    RELATIONSHIP_QUERY_TEXTBOX = (By.XPATH, "//textarea[@id='arid_WIN_0_304328790']")

    RELATIONSHIP_ADVANCE_SEARCH_BTN = (
        By.XPATH, "//a[@id='WIN_0_301867800']//div[@class='f1'][contains(text(),'Search')]")

    RELATIONSHIP_ROBI_AXIATA = (By.XPATH, "//*[contains(text(), 'Robi-Axiata')]")

    RELATE_THE_RELATIONSHIP_BTN = (By.XPATH, "//a[@id='WIN_0_301867500']//div[@class='f1']")

    RELATION_NEW_WINDOW_CLOSE_BTN = (By.XPATH, "//div[@class='f1'][contains(text(), 'Close')]")

    ALL_CHANGE_TABLE = (By.XPATH, "//table[@id='T301444200']//td[1]//nobr[1]//span")


class CloseChangeLocators(object):
    """ This Class is going to store all the required new Locators for Closing a Change Request """

    CHANGE_REQUEST_OPEN = (By.XPATH, "//input[@id = 'arid_WIN_3_1000000348']")
    CLOSE_MENU_SELECT = (By.XPATH, "//input[@id= 'arid_WIN_4_7']")
    SELECT_CLOSE_FROM_LST = (By.XPATH, "//tr[@class='MenuTableRow']//td[contains(text(), 'Closed')]")
    TASK_INIT_STATUS = (By.XPATH, "//input[@id='arid_WIN_4_7']")
    NEXT_STAGE_BUTTON = (By.XPATH, "//div[@class='f7'][contains(text(), 'Next Stage')]")
    CHANGE_STATUS_INPUT = (By.XPATH, "//input[@id='arid_WIN_4_7']")

    START_TIME_IN_TASK = (By.XPATH, "//input[@id='arid_WIN_4_1000000350']")
    END_TIME_IN_TASK = (By.XPATH, "//input[@id= 'arid_WIN_4_1000000362']")
    CLOSE_START_DATE = (By.XPATH, "//input[@id = 'arid_WIN_4_1000000348']")
    CLOSE_END_DATE = (By.XPATH, "//input[@id = 'arid_WIN_4_1000000364']")

    # Below is a special requirement where i need a changeable XPATH
    @staticmethod
    def get_changeable_xpath(dynamic_xpath: str) -> tuple:
        """ A static function to create a dynamic XPATH as user need while run time """
        return By.XPATH, dynamic_xpath


class CancelRequestLocators(object):
    """ A class variable holder for Canceling the Change Request """
    CHANGE_MANAGEMENT_CONSOLE = (By.XPATH, "//*[text()='Change Management Console']")
    MENU_FOR_STATUS = (By.XPATH, "//div[@id='WIN_3_303502600']//a[@class='btn btn3d menu']")
    SELECT_CANCEL = (By.XPATH, "//td[@class='MenuEntryNameHover']")
    CANCEL_OPTION_SELECT = (By.XPATH, "//td[contains(text(),'Cancel')]")
    SAVE = (By.XPATH, "//a[@id='WIN_3_1003']//div[@class='f1'][contains(text(),'Save')]")
    STATUS_AREA = (By.XPATH, "//textarea[@id='arid_WIN_3_303502600']")
