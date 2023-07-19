import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver



    def page_scroll(self):
            '''Slowly scrolls to the bottom of the page'''
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(1)
                pageLength = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        '''Extarnalization of webdriver wait'''
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        '''Extarnalization of webdriver wait'''
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def get_current_url(self):
        '''Method get current url'''
        get_url = self.driver.current_url
        print('Current url ' + get_url)


    def check_text(self, word, value):
        '''In case you want your case to go on regardless of failrure'''

        try:
            assert word.text == value
            print('Word value test passed')
        except AssertionError:
            print(f'Error! Value: {word.text} didn\'t match the value:{value}')
        print(f'passed word checked text:{word.text}, result: {value}')

    def assert_text(self, word, value):
        '''The same as (check text) but it doesn't convert the elem value to text'''
        try:
            assert word == value
            print('Word value pass')
        except AssertionError:
            print(F'Word value fail word: {word} result: {value}')
        print(f'passed word:{word}, result: {value}')

    def check_value(self, word, value):
        '''Tesing stops if there is a failure'''
        assert word.text == value
        print(f'Word value {value} test passed')


    def screenshot(self):
        '''Method make screenshot'''
        now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S')
        name_screenshot = 'screenshot' + str(now_date) + '.png'  # setting the proper file name and format
        self.driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\Selenium Python automation project\\screen\\' + name_screenshot)

    def assert_url(self,result):
        '''Mehtod to assert browers's current url'''
        current_url =  self.driver.current_url
        assert current_url == result, 'Wrong url!'
        print(f'Url test passed current url:{current_url} = expected url {result}')


    def assert_final_cart_price_subtotal(self,price,subtotal):
        '''Method that correctly extracts the subtotal value'''
        subtotal = subtotal[12:]
        print('Pass')
        print(f'Subtotal:{subtotal}')
        assert price == subtotal


    def assert_value_of_css_property(self,element,property,value):
        '''Method that extracts and tests element's property value'''
        element = element.get_attribute(property)
        print(f'Property:{element}')
        assert property == value, 'Element\'s property doesn\'t match'


