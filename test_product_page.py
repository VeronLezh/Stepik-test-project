from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import faker

Link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6",pytest.param("7", marks=pytest.mark.xfail(reason="Bug in WIP")), "8", "9"])
    #def test_guest_can_add_product_to_basket(browser, promo_offer):
        #ProductLink = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        #page = ProductPage(browser, ProductLink)
        #page.open()
        #page.add_product_to_basket()
        #page.solve_quiz_and_get_code()
        #page.should_be_product_is_in_basket()
        #page.should_be_equal_price()

def test_guest_cant_see_success_message(browser):
        page = ProductPage(browser, Link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_not_be_items_in_basket()

@pytest.mark.Auth
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(faker.Faker().email(), "QA_test123")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser,setup):
        product_page = ProductPage(browser, Link)
        product_page.open()
        product_page.should_not_be_success_message()
        
    def test_user_can_add_product_to_basket(self,browser,setup):
        product_page = ProductPage(browser, Link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_be_product_is_in_basket()
        product_page.should_be_equal_price()