from selenium.webdriver.common.by import By


class Login:
    # --- Locators ---
    email_id = "input-email"
    password_id = "input-password"
    login_button_css = "[value='Login']"
    incorrect_credentials_warning_css = "[id='account-login'] [class*='alert']"

    def __init__(self, driver):
        self.driver = driver

    # --- Page interactions ---
    def enter_email(self, email):
        return self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_password(self, password):
        return self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.login_button_css).click()

    def validate_incorrect_credentials_warning(self, message):
        return self.driver.find_element(By.CSS_SELECTOR, self.incorrect_credentials_warning_css).text. \
            __contains__(message)
