from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def go_to_basket_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET_BUTTON).click()

    def should_be_add_right_product(self):
        name = self.browser.find_element(*BasketPageLocators.BASKET_NAME).text
        name_add = self.browser.find_element(*BasketPageLocators.BASKET_ADD).text
        assert name == name_add, "Is not true name"

    def should_be_true_value(self):
        price = self.browser.find_element(*BasketPageLocators.BASKET_VALUE)
        price_add = self.browser.find_element(*BasketPageLocators.BASKET_VALUE_ADD)
        assert price.text == price_add.text, "is not true value"




