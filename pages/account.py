from selenium.webdriver.common.by import By


class MyAccount:
    # --- Locators ---
    view_order_history_link_text = "View your order history"

    def __init__(self, driver):
        self.driver = driver

    # --- Page interactions ---
    def validate_order_history_link_is_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, self.view_order_history_link_text).is_displayed()
