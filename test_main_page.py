from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"
linkLogin= "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_check_login_link(browser):
    page = LoginPage(browser,linkLogin)
    page.open()
    page.should_be_login_url()

def test_guest_can_see_login_form(browser):
    page = LoginPage(browser, linkLogin)
    page.open()
    page.should_be_login_form()

def test_guest_can_see_register_form(browser):
    page = LoginPage(browser, linkLogin)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_not_be_items_in_basket()