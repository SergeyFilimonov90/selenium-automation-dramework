import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import ClientInformationPageLocators
from utilities.utils import Utils


class ClientInformationPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Getters

    def get_first_name_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, ClientInformationPageLocators.FIRST_NAME)


    def get_last_name_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, ClientInformationPageLocators.LAST_NAME)


    def get_postal_code_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, ClientInformationPageLocators.POSTAL_CODE)


    def get_continue_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, ClientInformationPageLocators.CONTINUE_BUTTON)


    def get_client_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, ClientInformationPageLocators.CHECKOUT_PARAGRAPH)


    #Actions

    def input_first_name(self,first_name):
        self.get_first_name_field().send_keys(first_name)
        self.log.debug(f'Input first name: {first_name}')
        print('Input first_name')

    def input_last_name(self,last_name):
        self.get_last_name_field().send_keys(last_name)
        self.log.debug(f'Input first name: {last_name}')
        print('Input last_name')

    def input_postal_code(self,postal_code):
        self.get_postal_code_field().send_keys(postal_code)
        self.log.debug(f'Input postal code: {postal_code}')
        print('Input postal code')

    def click_continue(self):
        self.get_continue_button().click()
        self.log.debug(f'Clicked continue button')
        print('Clicked continue button')

    #Methods

    def client_page_test(self):
        Utils.add_start_step(method='client_page_test')
        self.check_text(self.get_client_text(),'Checkout: Your Information')
        self.input_first_name('Frank')
        self.input_last_name('Elgyn')
        self.input_postal_code('14546256')
        self.click_continue()
        Utils.add_end_step(url=self.driver.current_url, method='client_page_test')


