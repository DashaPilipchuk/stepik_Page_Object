from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    basket_p = BasketPage(browser, link)
    bp = BasePage(browser, link)
    bp.should_be_basket_page(*BasketPageLocators.BASKET_FOR_MAIN_PAGE)
    basket_p.should_be_empty_basket()
    basket_p.should_be_basket_without_items()


