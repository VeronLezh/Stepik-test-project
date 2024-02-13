from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
	def add_product_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

	def should_be_product_is_in_basket(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT).text
		print(product_name, message)
		assert message == product_name, f"{product_name} is not {message}"

	def should_be_equal_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert product_price == basket_price, f"{product_price} not equal {basket_price}"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
       		"Success message is presented, but should not be"
	def should_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), \
       		"Success message is not disappeared, but should be"