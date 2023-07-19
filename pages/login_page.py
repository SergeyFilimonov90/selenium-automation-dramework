from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.locators import LoginPageLocators
from utilities.utils import Utils




class Login_page(BaseDriver):

    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Utils()

    #Getters

    def get_user_name(self):
        return self.wait_until_element_is_clickable(By.XPATH,LoginPageLocators.USER_NAME)

    def get_password(self):
        return self.wait_until_element_is_clickable(By.XPATH,LoginPageLocators.PASSWORD_FIELD)

    def get_login_button(self):
        return self.wait_until_element_is_clickable(By.XPATH,LoginPageLocators.LOGIN_BUTTON)

    def get_message_container(self):
        return self.wait_until_element_is_clickable(By.XPATH, LoginPageLocators.MESSAGE_CONTAINER)

    def get_error_message(self):
        return self.wait_until_element_is_clickable(By.XPATH, LoginPageLocators.ERROR_MESSAGE)


    #Actions

    def input_user_name(self,user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user_name')
        self.log.debug(f'Input user_name{user_name}')

    def input_password(self,password):
        self.get_password().send_keys(password)
        print('Input password')
        self.log.debug(f'Input password{password}')

    def click_login_button(self):
        self.get_login_button().click()
        print('clicking button')
        self.log.debug('clicked login button')


    def authorization(self):
        Utils.add_start_step(method='authorization')
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
        Utils.add_end_step(url=self.driver.current_url, method='authorization')





