from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.url
        assert '/login/' in current_url, '/login is absent in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Register form is not present'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT)
        input_confirm_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        submit_button.click()
