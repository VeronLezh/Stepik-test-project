from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6",pytest.param("7", marks=pytest.mark.xfail(reason="Bug in WIP")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    ProductLink = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, ProductLink)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_is_in_basket()
    page.should_be_equal_price()