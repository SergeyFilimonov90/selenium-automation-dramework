import logging
import pytest
import softest
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils
from pages.login_page import Login_page
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.cart_step_two_page import Cart_final_page
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger(logLevel=logging.DEBUG)
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Login_page(self.driver) #composition
        self.ut = Utils()

    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\python-selenium\\TestFrameworkDemo\\testdata\\tdataexcel.xlsx", "Sheet1"))
    # @data(*Utils.read_data_from_csv("C:\\python-selenium\\TestFrameworkDemo\\testdata\\tdatacsv.csv"))
    # @unpack
    def test_smoke(self):
        smoke = Login_page(self.driver)
        smoke.authorization()
        main_page = MainPage(self.driver)
        main_page.select_product_1()
        cart_page = CartPage(self.driver)
        cart_page.cart_test_product_1()
        client_information_page = ClientInformationPage(self.driver)
        client_information_page.client_page_test()
        cart_page2 = Cart_final_page(self.driver)
        cart_page2.cart_step_2_test_product_1()
        finish = FinishPage(self.driver)
        finish.finish()










