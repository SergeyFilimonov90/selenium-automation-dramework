import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import FinishPageLocators
from utilities.utils import Utils


class FinishPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Getters

    def get_thank_you_header(self):
        return self.wait_until_element_is_clickable(By.XPATH, FinishPageLocators.THANK_YOU_HEADER)


    def get_thank_you_text(self):
        return self.wait_until_element_is_clickable(By.XPATH, FinishPageLocators.THANK_YOU_TEXT)


    def get_finish_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, FinishPageLocators.BACK_HOME_BUTTON)


    #Methods

    def click_finish_button(self):
        self.get_finish_button().click()
        self.log.debug('Clicked finish button')


    def finish(self):
        Utils.add_start_step(method='finish')
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.check_value(self.get_thank_you_header(),'Thank you for your order!')
        self.check_value(self.get_thank_you_text(),'Your order has been dispatched, and will arrive just as fast as the pony can get there!')
        self.click_finish_button()
        self.assert_url('https://www.saucedemo.com/inventory.html')
        self.screenshot()
        Utils.add_end_step(url=self.driver.current_url, method='finish')
