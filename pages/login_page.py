from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "It is not a login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"

    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.USER_FORM).click()
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys("123qwe1235")
        self.browser.find_element(*LoginPageLocators.PASSWORD_2).send_keys("123qwe1235")
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()





