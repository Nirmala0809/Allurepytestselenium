import pytest
from pages.login_page import LoginPage
from utilities.Utils import read_config_data_given_keys
from data_generator import menu_navigation_test_data as menu_data


@pytest.mark.usefixtures("driver_init")
class TestMenuNavigation:
    login_data = read_config_data_given_keys('LOGIN_PASS', 'username', 'password')

    menu_nav_data = menu_data.get_menuNavigation_testdata()

    @pytest.fixture(autouse=True)
    def load_url(self, driver_init, ):
        self.driver.delete_all_cookies()
        self.login_page = LoginPage(self.driver)
        self.logger.info("Loading URL")
        self.login_page.load()
        self.logger.debug(self.login_data)
        self.home_page = self.login_page.login_pass(self.login_data['username'], self.login_data['password'])
        self.logger.info("Login_Page - signin")

    @pytest.mark.sanity
    @pytest.mark.parametrize("navigation,expected_url", menu_nav_data['menu_navigation_data'])
    def test_menu_click(self, navigation, expected_url):
        self.home_page.menu_page.move_to_menu_and_click(navigation)
        assert self.driver.current_url == expected_url
