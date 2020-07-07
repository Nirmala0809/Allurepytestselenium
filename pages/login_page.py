from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from utilities import Utils


class LoginPage(BasePage):
    # url
    url = "https://opensource-demo.orangehrmlive.com/"

    # locators
    id_username = By.ID, "txtUsername"
    name_passwd = By.NAME, "txtPassword"
    class_login = By.CLASS_NAME, "button"
    id_error_msg = By.ID, "spanMessage"

    def __init__(self, driver, name="LoginPage", url=url):
        self.driver = driver
        self.name = name
        self.url = url

    def set_username(self, username):
        self.get_element(self.id_username).send_keys(username)

    def set_password(self, password):
        self.get_element(self.name_passwd).send_keys(password)

    def press_login(self):
        self.get_element(self.class_login).click()

    def login_fail(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.press_login()
        return LoginPage(self.driver)

    def login_pass(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.press_login()
        return HomePage(self.driver)

    def get_err_msg(self):
        return self.get_element(self.id_error_msg).text
