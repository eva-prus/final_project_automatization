from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_correct_name(self):
        name_alarm = self.browser.find_element(*ProductPageLocators.ALARM_NAME_PRODUCT).text
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name_alarm==name_product, 'Имя продукта на карточке и в сообщении не совпадает'

    def should_be_correct_price(self):
        price_alarm = self.browser.find_element(*ProductPageLocators.ALARM_PRICE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_alarm==price_product, 'Цена продукта на карточке и в сообщении не совпадает'