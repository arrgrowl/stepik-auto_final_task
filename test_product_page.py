import time

import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

BASE_URL = 'http://selenium1py.pythonanywhere.com'


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, BASE_URL)
        self.login_page.open()
        self.login_page.go_to_login_page()
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.go_to_product_page()
        page.add_product_to_basket()
        page.checking_message_that_product_is_added_to_basket()
        page.checking_message_about_basket_total()
        page.comparing_product_title()
        page.comparing_product_price()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.go_to_product_page()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.checking_message_that_product_is_added_to_basket()
    page.checking_message_about_basket_total()
    page.comparing_product_title()
    page.comparing_product_price()


def test_should_be_the_same_title_of_product(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.solve_quiz()
    page.comparing_product_title()


def test_should_be_the_same_price_between_product_and_adding_it_to_bucket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.solve_quiz()
    page.comparing_product_price()


def test_should_not_be_success_message_before_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.should_disappear_success_message()


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
    page.go_to_login_page()
    page = LoginPage(browser, url=browser.current_url)
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, url=browser.current_url)
    page.should_be_basket_page()
    page.should_be_empty_basket()
    page.should_be_message_about_empty_basket()
