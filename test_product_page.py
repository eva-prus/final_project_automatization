from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.login_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.login_page = LoginPage(browser,link)
        self.login_page.open()
        email_test = str(time.time()) + "@fakemail.org"
        password_test = str(time.time())
        self.login_page.register_new_user(email=email_test,password=password_test)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        current_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,current_link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        current_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,current_link)
        page.open()
        page.should_be_add_to_cart()
        page.should_be_correct_name()
        page.should_be_correct_price()

    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    current_link = link
    page = ProductPage(browser,current_link)
    page.open()
    page.should_be_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    current_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,current_link)
    page.open()
    page.should_be_add_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    current_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,current_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    current_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,current_link)
    page.open()
    page.should_be_add_to_cart()
    page.should_be_disappered_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_go_to_basket()
    page.should_not_be_products_in_basket()
    page.should_be_presented_message_about_empty_basket()

