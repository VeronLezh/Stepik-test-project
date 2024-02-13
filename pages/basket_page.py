from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): 
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are in the basket,but should not be"