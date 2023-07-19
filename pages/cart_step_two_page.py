import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import  CartStepTwoLocators
from pages.main_page import MainPage
from utilities.utils import Utils


class Cart_final_page(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_checkout_overview_paragraph_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.PARAGRAPH)


    def get_product_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.PRODUCT_NAME)

    def get_product_price(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.PRODUCT_PRICE)

    def get_subtotal_price(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.SUBTOTAL_PRICE)

    def get_finish_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.FINISH_BUTTON)

    def get_tax(self):
        tax = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.TAX)
        tax_text = tax.text[6:]
        print(tax_text)
        return tax_text


    def get_total(self):
        total = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.TOTAL_PRICE)
        total_text = total.text[8:]
        return total_text

    def get_products_price_subtotal_numeric(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.SUBTOTAL_PRICE)
        product_subtotal_price_numeric = product1.text[13:]
        print(f'Subtotal: {product_subtotal_price_numeric}')
        return product_subtotal_price_numeric


    def get_products_name_cart(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.PRODUCT_NAME)
        product_name = product1.text
        print(f'Product name: {product_name}')
        self.log.debug(f'Cart step two product 1 name: {product_name}')
        return product_name


    def get_products_price_cart(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.PRODUCT_PRICE)
        product_price = product1.text
        print(f'Price: {product_price}')
        self.log.debug(f'Cart step two product 1 price: {product_price}')
        return product_price

    def get_products_pricesubtotal_cart(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, CartStepTwoLocators.SUBTOTAL_PRICE)
        product_subtotal_price = product1.text[12:]
        print(f'Subtotal: {product_subtotal_price}')
        self.log.debug(f'Subtotal: {product_subtotal_price}')
        return product_subtotal_price

    #Actions
    def click_final_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    #Methods

    def cart_step_2_test_product_1(self):
        Utils.add_start_step(method='cart_step_2_test_product_1')
        self.get_current_url()
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(MainPage.product_1_text, self.get_products_name_cart())
        self.assert_text(MainPage.product_1_price, self.get_products_price_cart())
        self.assert_text(MainPage.product_1_price,self.get_products_pricesubtotal_cart())
        self.click_final_finish_button()
        Utils.add_end_step(url=self.driver.current_url, method='cart_step_2_test_product_1')

