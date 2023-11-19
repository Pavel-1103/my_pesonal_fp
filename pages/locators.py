from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_SINGUP = (By.XPATH, "//li[@class = 'dropdown inuser']")
    LOGIN_BUTTON = (By.XPATH, "//li[@class = 'dropdown inuser open']")
    LOGOUT = (By.XPATH, "//a[@class = 'list-group-item logu']")
    CABINET = (By.XPATH, "//li[@class = 'dropdown inuser']")
    CONTACTS = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[6]/a")
    BLOG = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[5]/a")
    PAYMENT = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[4]/a")
    DELIVERY = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[3]/a")
    ABOUT = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[2]/a")
    MAIN = (By.XPATH, "//*[@id='right-colume-1']/ul[1]/li[1]/a")

    LANGUEGE_BTN = (By.XPATH, "//*[@id='form-language']/div/button")
    UKRAINIAN_LANG = (By.XPATH, "//*[@id='form-language']/div/ul/li[1]/button")
    RUSSIAN_LANG = (By.XPATH, "//*[@id='form-language']/div/ul/li[2]/button")
    INSTA_BTN = (By.XPATH, "//a[@href = 'https://www.instagram.com/trium.ua/']")
    FB_BTN = (By.XPATH, "//a[@href = 'https://www.facebook.com/trium.ua/']")
    LOGO_DESK = (By.XPATH, "//*[@class='col-md-3 col-sm-2 col-xs-2 hlogo']/img[@src = 'image/catalog/logo_trium.svg']")
    COMPARISON = (By.XPATH, "//a[@href = 'compare']")
    CART = (By.XPATH, "//div[@class = 'por custom_cart']")
    HITS = (By.XPATH, "//*[@id='content']/div[3]/div/div")
    ADVERTISING_UNIT = (By.XPATH, "//div[@class = 'homeslider-container s-panel']")
    NEW_NOUT_CAT = (By.XPATH, "//span[text() = 'Ноутбуки']")
    USED_NOUT_CAT = (By.XPATH, "//span[text() = 'Ноутбуки б/в']")


class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//*[@id='content']/div[1]/div/div/div[2]")
    CAT_SPARE_PARTS = (By.XPATH, "//a[text() = 'Запчастини для ноутбуків б/в']/div")
    SUB_CAT_SPARE_PARTS = (By.XPATH, "//a[@href = 'zapchast-n-dlja-noutbukiv-b-v/zapchast-n-bjez-foto/']")

    DELIVERY_BLOCK = (By.XPATH, "//div[@class='col-md-4 col-sm-4 col-xs-12 fborder']/div[@class='collapse footer-collapse']/ul[@style]/li[2]/a[@href='dostavka']")
    ABOUT_BLOCK = (By.XPATH, "//div[@class='col-md-4 col-sm-4 col-xs-12 fborder']/div[@class='collapse footer-collapse']/ul[@style]/li[1]/a[@href='about']")
    PAYMENT_BLOCK = (By.XPATH, "//div[@class='col-md-4 col-sm-4 col-xs-12 fborder']/div[@class='collapse footer-collapse']/ul[@style]/li[3]/a[@href='oplata']")
    BLOG_BLOCK = (By.XPATH, "//div[@class='col-md-4 col-sm-4 col-xs-12 fborder']/div[@class='collapse footer-collapse']/ul[@style]/li[4]/a[@href='blog']")
    CONTACTS_BLOCK = (By.XPATH, "//div[@class='col-md-4 col-sm-4 col-xs-12 fborder']/div[@class='collapse footer-collapse']/ul[@style]/li[5]/a[@href='contacts']")
    SCROLL_TO_TOP_BTN = (By.XPATH, "//a[@title = 'Scroll to Top']")



class SignupLoginPageLocators:
    LOGIN_SINGUP = (By.XPATH, "//li[@class = 'dropdown inuser']")
    LOGIN_ICON = (By.XPATH, "//li[@class = 'dropdown inuser open']")
    ADD_LOGIN = (By.XPATH, "//div[@class = 'form-group']/input[@name = 'email']")
    ADD_PASSWORD = (By.XPATH, "//div[@class = 'form-group']/input[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")



   


class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, "//h4[@class='protitle']/a[@href = 'index.php?route=product/product&product_id=41989']")
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, "//button[@id='button-cart']")
    PRICE_FIRST_PRODUCT = (By.XPATH, "//h2[@class = 'pro-price']")
    BTN_CONTINUE_SHOP_POPUP = (By.XPATH, "//button[text()='Продовжити покупки']")

    SECOND_PRODUCT_INPUT = (By.XPATH, "//div[@class='caption']//a[@href='index.php?route=product/product&product_id=41988']")
    PRICE_SECOND_PRODUCT = (By.XPATH, "//h2[@class='pro-price']")
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, "//button[text()='Продовжити покупки']")
    TOTAL_PRICE = (By.XPATH, "//span[@id='cart-total']")
    



class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass