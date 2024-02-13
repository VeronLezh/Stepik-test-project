from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET = (By.CSS_SELECTOR,".basket-mini .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    REGISTER_FORM_PASSWORD =(By.CSS_SELECTOR,"#id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM =(By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    PRODUCT_NAME =(By.CSS_SELECTOR,".product_main > h1")
    ADD_TO_CART = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR,"div.alertinner > strong")
    PRODUCT_PRICE =(By.CSS_SELECTOR,".product_main>.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR,"div.alert div p strong")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS =(By.CSS_SELECTOR, ".basket-items")