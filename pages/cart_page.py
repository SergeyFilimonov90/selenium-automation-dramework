import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import CartStepOneLocators
from pages.main_page import MainPage
from utilities.utils import Utils


class CartPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Getters

    def get_product_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.PRODUCT_TEXT)


    def get_product_price(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.PRODUCT_PRICE)


    def get_paragraph_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.PARAGRAPH)


    def get_checkout_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.CHECKOUT_BUTTON)


    def get_products_price_1_cart(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.PRODUCT_PRICE)
        product1_price_cart = product1.text
        print(f'cart page price: {product1_price_cart}')
        self.log.debug(f'cart page price: {product1_price_cart}')
        return product1_price_cart

    def get_products_text_1_cart(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepOneLocators.PRODUCT_TEXT)
        product1_text_cart = product1.text
        print(f'cart page text: {product1_text_cart}')
        self.log.debug(f'cart page name: {product1_text_cart}')
        return product1_text_cart

    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Item added to cart')
        self.log.debug(f'Item added to cart')

    #Methods

    def cart_test_product_1(self):
        Utils.add_start_step(method='cart_test_product_1')
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/cart.html')
        self.get_products_text_1_cart()
        self.get_products_price_1_cart()
        self.assert_text(MainPage.product_1_text, self.get_products_text_1_cart())
        self.assert_text(MainPage.product_1_price,self.get_products_price_1_cart())
        self.click_checkout_button()
        Utils.add_end_step(url=self.driver.current_url, method='cart_test_product_1')

