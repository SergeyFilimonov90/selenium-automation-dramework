import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import MainPageLocators
from utilities.utils import Utils


class MainPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    product_1_price = ''

    product_1_text = ''

    def get_products_paragraph_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.PARAGRAPH)

    def set_product_1_price(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.PRICE)
        MainPage.product_1_price = product1.text
        print(f'Global price:{self.product_1_price}')
        self.log.debug(f'Global price:{self.product_1_price}')
        return MainPage.product_1_price

    def set_product_1_text(self):
        product1 = self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.PRODUCT)
        MainPage.product_1_text = product1.text
        print(f'Global name:{self.product_1_text}')
        self.log.debug(f'Global product1 name:{self.product_1_price}')
        return MainPage.product_1_text


    # Getters

    def get_product_1_text_main_page(self):
        return self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.PRODUCT)


    def get_product_1_price(self):
        return self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.PRODUCT)


    def get_add_to_cart_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.ADD_TO_CART_BUTTON)


    def get_cart_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, MainPageLocators.CART_ICON)

    # Actions

    def add_to_cart_button_click(self):
        self.get_add_to_cart_button().click()
        print('Clicked add to cart button')
        self.log.debug('Clicked add to cart button')

    def cart_icon_click(self):
        self.get_cart_icon().click()
        print('Click cart icon')
        self.log.debug('Clicked cart icon')

    # Methods

    def select_product_1(self):
        Utils.add_start_step(method='select_product_1')
        self.assert_url('https://www.saucedemo.com/inventory.html')
        self.check_text(self.get_products_paragraph_text(), 'Products')
        self.set_product_1_price()
        self.set_product_1_text()
        self.add_to_cart_button_click()
        self.check_text(self.get_cart_icon(), '1')
        self.cart_icon_click()
        Utils.add_end_step(url=self.driver.current_url, method='select_product_1')


