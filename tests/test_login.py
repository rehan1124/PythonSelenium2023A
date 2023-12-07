import pytest

from pages.account import MyAccount
from pages.navigation import NavigationBar
from tests.base_test import BaseTest
from utilities.utilities import generate_email_with_timestamp, get_row_values


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email, password", [get_row_values("TestData/test_login.xlsx", "Sheet1", "Scenario1"),
                                                 get_row_values("TestData/test_login.xlsx", "Sheet1", "Scenario2"),
                                                 get_row_values("TestData/test_login.xlsx", "Sheet1", "Scenario3")])
    def test_valid_login(self, email, password):
        """
        Test to validate login with correct credentials
        :return:
        """

        myaccount_driver = MyAccount(self.driver)
        navigationbar_driver = NavigationBar(self.driver)

        # Perform actions on portal
        navigationbar_driver.click_my_account_dropdown()
        self.take_screenshot()
        login_driver = navigationbar_driver.click_login_menu_item()
        self.take_screenshot()

        # email = "sr24111989@gmail.com"
        # password = "Selenium0987@"

        login_driver.enter_email(email)
        login_driver.enter_password(password)
        self.take_screenshot()
        login_driver.click_login_button()

        # Assertions
        assert myaccount_driver.validate_order_history_link_is_displayed()

        self.take_screenshot()

    def test_valid_email_invalid_password(self):
        """
        Test to validate warning message when correct email with incorrect password is entered.
        :return:
        """
        navigationbar_driver = NavigationBar(self.driver)

        # Perform actions on portal
        navigationbar_driver.click_my_account_dropdown()
        login_driver = navigationbar_driver.click_login_menu_item()

        email = "aaa1@gmail.com"
        password = "Selenium"

        self.take_screenshot()
        login_driver.enter_email(email)
        login_driver.enter_password(password)
        self.take_screenshot()
        login_driver.click_login_button()

        # Assertions
        assert login_driver.validate_incorrect_credentials_warning(
            "Warning: No match for E-Mail Address and/or Password.")

        self.take_screenshot()

    def test_invalid_email_valid_password(self):
        """
        Test to validate message when incorrect email and password is entered.
        :return:
        """
        navigationbar_driver = NavigationBar(self.driver)

        # Perform actions on portal
        navigationbar_driver.click_my_account_dropdown()
        login_driver = navigationbar_driver.click_login_menu_item()

        email = generate_email_with_timestamp()
        password = "Selenium"

        login_driver.enter_email(email)
        login_driver.enter_password(password)
        self.take_screenshot()
        login_driver.click_login_button()

        # Assertions
        assert login_driver.validate_incorrect_credentials_warning(
            "Warning: No match for E-Mail Address and/or Password.")

        self.take_screenshot()
