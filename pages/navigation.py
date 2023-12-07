from selenium.webdriver.common.by import By

from pages.login import Login
from pages.registration import AccountRegistration


class NavigationBar:
    # --- Locators ---
    my_account_dropdown = "[title='My Account']"
    login_menu_item = "a[href*='account/login']"
    register_menu_item = "a[href*='account/register']"

    def __init__(self, driver):
        self.driver = driver

    # --- Page interactions ---
    def click_my_account_dropdown(self):
        self.driver.find_element(By.CSS_SELECTOR, self.my_account_dropdown).click()
        return

    def click_login_menu_item(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_menu_item).click()
        return Login(self.driver)

    def click_register_menu_item(self):
        self.driver.find_element(By.CSS_SELECTOR, self.register_menu_item).click()
        return AccountRegistration(self.driver)
