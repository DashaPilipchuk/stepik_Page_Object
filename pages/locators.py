from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    USER_FORM = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BASKET_NAME = (By.CSS_SELECTOR, "#content_inner > article > div:nth-child(1) > div.col-sm-6.product_main > h1")
    BASKET_ADD = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_VALUE = (By.CSS_SELECTOR, "#content_inner > article > div:nth-child(1) > div.col-sm-6.product_main > "
                                     "p.price_color")
    BASKET_VALUE_ADD = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                         "p:nth-child(1) > strong")
    BASKET_FOR_MAIN_PAGE = (By.CSS_SELECTOR, "body > header > div.page_inner > div > "
                                             "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_FOR_PRODUCT_PAGE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > "
                                                "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#logout_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")