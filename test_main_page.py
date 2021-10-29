from pages.base_page import BasePage
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()  # открываем страницу
	login_page = page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
	login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = BasePage(browser, link)
	page.open()
	page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/'
	page = BasePage(browser, link)
	page.open()
	page.go_to_basket_page()
	page = BasketPage(browser, url=browser.current_url)
	page.should_be_basket_page()
	page.should_be_empty_basket()
	page.should_be_message_about_empty_basket()
