from common_methods.common_methods import CommonMethods
from pages.navigation import NavigationBar
from tests.base_test import BaseTest
from utilities.utilities import generate_email_with_timestamp, generate_random_string


class TestRegister(BaseTest):
    def test_register_user(self):
        """
        Test to make a valid new user registration with all details.
        :return:
        """
        navigationbar_driver = NavigationBar(self.driver)
        commonmethods_driver = CommonMethods(self.driver)

        navigationbar_driver.click_my_account_dropdown()
        accountregistration_driver = navigationbar_driver.click_register_menu_item()

        first_name = generate_random_string()
        last_name = generate_random_string()
        email = generate_email_with_timestamp()
        telephone = "9999999999"
        password = generate_random_string()
        print(f"Name: {first_name} {last_name}; email: {email}")

        self.take_screenshot()

        commonmethods_driver.new_user_registration(first_name, last_name, email, telephone, password, password, "yes")
        self.take_screenshot()

        accountregistration_driver.click_continue_button()

        success_message = "Your Account Has Been Created!"

        assert accountregistration_driver.validate_account_creation_message(success_message)
        print(f"Validate success message <{success_message}> is displayed on web-page.")

        self.take_screenshot()
