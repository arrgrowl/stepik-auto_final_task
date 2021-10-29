from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_TITLE_ON_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) > div > strong')
    PRODUCT_PRICE_ON_MESSAGE = (By.CSS_SELECTOR, '#messages p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) > div')
    MESSAGE_FOR_AMOUNT_OF_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(3) p')
