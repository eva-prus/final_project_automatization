from .base_page import BasePage
from .locators import BasketPageLocators    


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.ITEM_ROW) 

    def should_be_presented_message_about_empty_basket(self):
        self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)