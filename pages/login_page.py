from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_enter = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_enter.send_keys(email)
        password_enter = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_enter.send_keys(password)
        password_retry_enter = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_RETRY)
        password_retry_enter.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        now_url = self.browser.current_url
        assert 'login' in now_url, 'Подстрока "login" отсутствует в текущем url браузера'

    def should_be_login_form(self):
        login_form = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert login_form != [], "Форма логина не найдена"

    def should_be_register_form(self):
        registration_form = self.browser.find_elements(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form !=[], "Форма регистрации не найдена"
