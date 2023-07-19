

class LoginPageLocators:
    USER_NAME = "//input[@ID='user-name']"
    PASSWORD_FIELD = "//input[@ID='password']"
    LOGIN_BUTTON = "//input[@value='Login']"
    MESSAGE_CONTAINER = "//div[@class='error-message-container error']"
    ERROR_MESSAGE = "//h3[@data-test='error']"


class MainPageLocators:
    PARAGRAPH = "//span[@class='title']"
    PRODUCT = "//*[@id='item_4_title_link']/div"
    PRICE = "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
    ADD_TO_CART_BUTTON = "//button[@id='add-to-cart-sauce-labs-backpack']"
    CART_ICON = "//span[@class='shopping_cart_badge']"

class CartStepOneLocators:
    PARAGRAPH = "//span[@class='title']"
    PRODUCT_TEXT = "//div[@class='inventory_item_name']"
    PRODUCT_PRICE = "//div[@class='inventory_item_price']"
    CHECKOUT_BUTTON = "//button[@id='checkout']"


class ClientInformationPageLocators:
    CHECKOUT_PARAGRAPH = "//span[@class='title']"
    FIRST_NAME = "//input[@id='first-name']"
    LAST_NAME = "//input[@id='last-name']"
    POSTAL_CODE = "//input[@id='postal-code']"
    CONTINUE_BUTTON = "//input[@id='continue']"


class CartStepTwoLocators:
    PARAGRAPH = "//span[@class='title']"
    PRODUCT_NAME = "//div[@class='inventory_item_name']"
    PRODUCT_PRICE = "//div[@class='inventory_item_price']"
    SUBTOTAL_PRICE = "//div[@class='summary_subtotal_label']"
    TOTAL_PRICE = "//div[@class='summary_info_label summary_total_label']"
    TAX = "//div[@class='summary_tax_label']"
    FINISH_BUTTON = "//button[@id='finish']"

class FinishPageLocators:
    THANK_YOU_HEADER =  "//h2[@class='complete-header']"
    THANK_YOU_TEXT =  "//div[@class='complete-text']"
    BACK_HOME_BUTTON = "//button[@class='btn btn_primary btn_small']"
