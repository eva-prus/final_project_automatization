from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
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