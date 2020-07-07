from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MenuPage(BasePage):
    url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    # MenuPage locators

    menu_locators = {
        "Admin": (By.ID, "menu_admin_viewAdminModule"),
        "User Management": (By.ID, "menu_admin_UserManagement"),
        "Users": (By.ID, "menu_admin_viewSystemUsers"),
        "Job": (By.ID, "menu_admin_Job"),
        "Job Titles": (By.ID, "menu_admin_viewJobTitleList"),
        "Nationalities": (By.ID, "menu_admin_nationality"),

        "PIM": (By.ID, "menu_pim_viewPimModule"),
        "Add Employee": (By.ID, "menu_pim_addEmployee"),
        "Configuration": (By.ID, "menu_pim_Configuration"),
        "Data Import": (By.ID, "menu_admin_pimCsvImport")

    }

    def __init__(self, driver, name="MenuPage", url=url):
        self.driver = driver
        self.name = name
        self.url = url

    def move_to_menu_and_click(self, menus):
        menus = map(str.strip, menus.split(","))

        actions = ActionChains(self.driver)
        for menu in menus:
            actions.move_to_element(self.get_element(self.menu_locators[menu]))

        actions.click().perform()
