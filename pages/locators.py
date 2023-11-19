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
    #LOGO_MOB = (By.XPATH, "//div[@class='logo logo-mob']/a/ing")
    COMPARISON = (By.XPATH, "//a[@href = 'compare']")
    CART = (By.XPATH, "//div[@class = 'por custom_cart']")
    HITS = (By.XPATH, "//*[@id="content"]/div[3]/div/div")
    DISCOUNTS = (By.XPATH, "//a[@class='check-item check-sale']")
    NEW_ITEMS = (By.XPATH, "//a[@class='check-item']")
    SAMSUNG_CAT = (By.XPATH, "//div[text()='Samsung']")
    SAMSUNG_J701 = (By.XPATH, "//a[@href='BrandModel/Samsung-J701']")

    SUBSCRUBE = (By.XPATH, "//button[@class='newsletter_button']")
    INPUT_SUBSCRIBE = (By.XPATH,"//input[@class='newsletter_input']")
    LOGO_FOOT = (By.XPATH, "//img[@src='images/logo-footer.png']")
    ALERT_SUCCESS = (By.XPATH, "//div[@id = 'alert-success']")
    ALERT_ERROR = (By.XPATH, "//div[@id = 'alert-error']")



class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class='screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href='category/zaryadki']")
    SUB_CAT_POWER_BANK = (By.XPATH, "//ul[@class='cat_menu']/li[5]/ul/li[6]")

    INFO_BLOCK_VOZVRAT_SREDSTV = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[1]/div")
    INFO_BLOCK_DOSTAVKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[2]/div")
    INFO_BLOCK_OTSROCHKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[3]/div")
    INFO_BLOCK_SUPPORT = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[4]/div")
    BUTTON_SHOW_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals_title clearfix']//a[@href='main/showNew']")
    BUTTON_PREV_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_prev']")
    BUTTON_NEXT_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_next']")
    SECTION_NEW_PRODUCTS = (By.XPATH, "//div[@class='nes_arrivals']//div[@class='slick-list draggable']")
    NEW_PRODUCT_8 = (By.XPATH, "//div[@class='new_arrivals']//div[@class='slick-list draggable']/div/div[3]div[2]")
    BUTTON_SHOW_HITS = (By.XPATH, "//div[@class='best_sellers']//a[@href='main/showHit']")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_prev best_nav']/i")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_next best_nav']/i")
    SECTION_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='bestsellers_panel panel_active']")
    BUTTON_PREV_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_prev trendsna_nav slick-arrow']/i")
    BUTTON_NEXT_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_next trends_nav slick-arrow']/i")


class SignupLoginPageLocators:
    GO_TO_SIGNUP = (By.XPATH, "//a[@href = 'user/signup']")
    H1_SIGNUP = (By.XPATH, "//h1[text() = 'Регистрация']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    BUTTON_SIGNUP = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    H1_VHOD = (By.XPATH, "//h1[text() = 'Вход']")
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")



class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]")
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//button[text() = 'В корзину!']")
    PRICE_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//div[@class = 'product_price']")
    BTN_CONTINUE_SHOP_POPUP = (By.XPATH, "//button[text() = 'Продолжить покупки']")
    SECOND_PRODUCT_INPUT_NUMBER_QTY = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//input[@type = 'number']")
    PRICE_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//div[@class = 'product_price']")
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//button")
    TOTAL_PRICE = (By.XPATH, "//tr[@class = 'cart-cena']/td[2]")
    QTY = (By.XPATH, "//tr[@class = 'cart-itogo']/td[2]")
    CHECKOUT_BTN_POPUP = (By.XPATH, "//a[@href = 'cart/view']")
    CART_REG_FORM = (By.XPATH, "//div[@class = 'cart-reg']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    INPUT_NOTE = (By.XPATH, "//textarea[@name= 'note']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class = 'btn green']")



class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass