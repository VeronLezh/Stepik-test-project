from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME =(By.CSS_SELECTOR,".product_main > h1")
    ADD_TO_CART = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR,".alertinner ")
    PRODUCT_PRICE =(By.CSS_SELECTOR,".product_main>.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR,".alertinner p23")