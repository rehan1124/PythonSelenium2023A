from selenium.webdriver.common.by import By


class AccountRegistration:
    # --- Locators ---
    firstname_input_id = "input-firstname"
    lastname_input_id = "input-lastname"
    email_input_id = "input-email"
    telephone_input_id = "input-telephone"
    password_input_id = "input-password"
    password_confirm_input_id = "input-confirm"
    agree_checkbox_name = "agree"
    continue_button_css = "input[value='Continue']"
    account_success_message_css = "[id='content'] h1"

    def __init__(self, driver):
        self.driver = driver

    # --- Page interactions ---
    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_input_id).send_keys(firstname)
        return

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_input_id).send_keys(lastname)
        return

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)
        return

    def enter_telephone_number(self, number):
        self.driver.find_element(By.ID, self.telephone_input_id).send_keys(number)
        return

    def enter_password(self, password, confirm_password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)
        self.driver.find_element(By.ID, self.password_confirm_input_id).send_keys(confirm_password)
        return

    def click_privacy_policy(self):
        self.driver.find_element(By.NAME, self.agree_checkbox_name).click()
        return

    def click_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_button_css).click()
        return

    def validate_account_creation_message(self, message):
        return self.driver.find_element(By.CSS_SELECTOR, self.account_success_message_css).text.__contains__(message)
