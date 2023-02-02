from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket not empty"

    def should_be_basket_without_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_VALUE_ADD), "Success message is presented, but " \
                                                                                  "should not be "
