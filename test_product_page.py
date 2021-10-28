from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.solve_quiz()
    page.checking_message_that_product_is_added_to_basket()
    page.checking_message_about_basket_total()


def test_should_be_the_same_title_of_product(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.solve_quiz()
    page.comparing_product_title()


def test_should_be_the_same_price_between_product_and_adding_it_to_bucket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.add_product_to_basket()
    page.solve_quiz()
    page.comparing_product_price()
