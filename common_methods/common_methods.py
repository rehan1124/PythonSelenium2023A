from pages.home_page import HomePage
from pages.registration import AccountRegistration


class CommonMethods:
    def __init__(self, driver):
        self.driver = driver
        self.homepage_driver = HomePage(self.driver)
        self.accountregistration_driver = AccountRegistration(self.driver)

    def search_product(self, product_name):
        self.homepage_driver.enter_text_in_search_box(product_name)
        self.homepage_driver.click_on_search_button()
        return

    def new_user_registration(self, firstname, lastname, email, telephone, password, confirm_password, privacy_policy):
        """

        :param firstname:
        :param lastname:
        :param email:
        :param telephone:
        :param password:
        :param confirm_password:
        :param privacy_policy: yes or no
        :return:
        """
        self.accountregistration_driver.enter_firstname(firstname)
        self.accountregistration_driver.enter_lastname(lastname)
        self.accountregistration_driver.enter_email(email)
        self.accountregistration_driver.enter_telephone_number(telephone)
        self.accountregistration_driver.enter_password(password, confirm_password)
        if privacy_policy == "yes":
            self.accountregistration_driver.click_privacy_policy()
        return
