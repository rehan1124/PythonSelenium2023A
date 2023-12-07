from selenium.webdriver.common.by import By


class HomePage:
    # --- Locators ---
    search_box_name = "search"
    search_button_css = "[id='search'] button"
    search_button_results = "//input[@id='button-search']/following-sibling::p"

    def __init__(self, driver):
        self.driver = driver

    # --- Web action implementations ---
    def enter_text_in_search_box(self, input_text):
        element = self.driver.find_element(By.NAME, self.search_box_name)
        element.send_keys(input_text)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
        return

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_css).click()
        return

    def validate_link_text_is_displayed(self, text):
        return self.driver.find_element(By.LINK_TEXT, text).is_displayed()

    def validate_no_product_search_results(self, expected_text):
        return self.driver.find_element(
            By.XPATH, self.search_button_results
        ).text.__eq__(expected_text)
