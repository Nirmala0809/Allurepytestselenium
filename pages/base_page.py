from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, name, url):
        self.name = name
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def load(self):
        # Utils.log("INFO", f"{self.name}, Loading")
        self.driver.get(self.url)

    def is_page_loaded(self):
        # Utils.log("INFO", f"Verifying {self.name}, loaded")
        result = False
        try:
            result = self.wait.until(EC.url_contains(self.url))
        except Exception as e:
            # Utils.log("ERROR", f"{self.name}, is not getting displayed; {e.__cause__}")
            pass
        return result

    def get_element(self, locator):
        try:
            element = self.driver.find_element(locator[0], locator[1])
        except Exception as e:
            # msg = f"{self.name}, element: {locator}, msg:{e.__class__}"
            # Utils.log("ERROR", msg)
            pass
        else:
            return element
