from common_methods.common_methods import CommonMethods
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    def test_search_valid_product(self):
        """
        Test to search for existing/valid product.
        :return:
        """
        home_page_driver = HomePage(self.driver)
        commonmethods_driver = CommonMethods(self.driver)

        # Search and validate
        validate_link_text = "HP LP3065"
        enter_search_text = "HP"

        # Perform actions on portal
        self.take_screenshot()
        commonmethods_driver.search_product(enter_search_text)

        # Assertions
        assert home_page_driver.validate_link_text_is_displayed(validate_link_text)
        print(f"Validated text {validate_link_text} is present on page.")
        self.take_screenshot()

        # assert False

    def test_search_invalid_product(self):
        """
        Test to search for invalid/non-existing product.
        :return:
        """
        home_page_driver = HomePage(self.driver)
        commonmethods_driver = CommonMethods(self.driver)

        # Search and validate
        expected_text = "There is no product that matches the search criteria."
        enter_search_text = "Honda"

        # Perform actions on portal
        commonmethods_driver.search_product(enter_search_text)

        assert home_page_driver.validate_no_product_search_results(expected_text)
        print(f"Validated text {expected_text} is present on page.")
        self.take_screenshot()

        # assert False

    def test_empty_search(self):
        """
        Test to validate results for empty search.
        :return:
        """
        home_page_driver = HomePage(self.driver)

        # Search and validate
        expected_text = "There is no product that matches the search criteria."

        # Perform actions on portal
        home_page_driver.click_on_search_button()

        assert home_page_driver.validate_no_product_search_results(expected_text)
        print(f"Validated text {expected_text} is present on page.")
        self.take_screenshot()

        # assert False
