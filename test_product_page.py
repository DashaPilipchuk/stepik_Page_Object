import pages.base_page
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from pages.basket_page import BasketPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    bp = BasePage(browser, link)
    bp.solve_quiz_and_get_code()
    page.should_be_add_right_product()
    page.should_be_true_value()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    basket_p = BasketPage(browser, link)
    bp = BasePage(browser, link)
    bp.should_be_basket_page(*BasketPageLocators.BASKET_FOR_PRODUCT_PAGE)
    basket_p.should_be_empty_basket()
    basket_p.should_be_basket_without_items()
