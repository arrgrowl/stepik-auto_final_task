from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        self.open()

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def checking_message_that_product_is_added_to_basket(self):
        self.browser.implicitly_wait(10)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_FOR_ADDING_PRODUCT_TO_BASKET), "There is no " \
                                                                                                   "message" \
                                                                                                   "about adding" \
                                                                                                   "product to basket" \
                                                                                                   "or product wasn't" \
                                                                                                   " added to basket"

    def checking_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ON_MESSAGE), 'There is no message about' \
                                                                                       'total amount of basket'

    def comparing_product_title(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_name_from_message = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_ON_MESSAGE).text
        assert product_name == product_name_from_message, 'There is wrong product added to bucket'

    def comparing_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_on_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_MESSAGE).text
        assert product_price == product_price_on_message, 'There is wrong price between product from page and' \
                                                          'this product after adding to bucket'
