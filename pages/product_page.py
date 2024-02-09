from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
	def add_product_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

	def should_be_product_is_in_basket(self):
		x_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		x = x_element.text
		y_element = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT)
		y=y_element.text
		assert x in y, "Неправильный товар добавлен в корзину"

	def should_be_equal_price(self):
		x_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		x = x_element.text
		y_element = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
		y=y_element.text
		assert x in y, "Стоимость товара и цена в корзине не совпадают"
