from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_RETRY = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-lg.btn-primary')
    ALARM_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    ALARM_PRICE = (By.CSS_SELECTOR, 'div.alert:nth-child(3) strong')
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main p.price_color')