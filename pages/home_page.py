from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.menu_page import MenuPage


class HomePage(BasePage):
    url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    # HomePage locators
    plt_welcome_msg = By.PARTIAL_LINK_TEXT, "Welcome "

    def __init__(self, driver, name="HomePage", url=url):
        self.driver = driver
        self.name = name
        self.url = url
        self.menu_page = MenuPage(self.driver)

    def get_wel_msg(self):
        return self.get_element(self.plt_welcome_msg).text
