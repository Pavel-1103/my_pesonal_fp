from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SINGUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_blog(self):
        assert self.hover_action(*locators.BasePageLocators.CONTACTS), \
            "Element 'Контакти' is not present"
        assert self.is_element_present(*locators.BasePageLocators.BLOG), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.CONTACTS), \
            "Element 'Контакти' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_about(self):
        assert self.hover_action(*locators.BasePageLocators.CONTACTS), \
            "Element 'Контакти' is not present"
        assert self.is_element_present(*locators.BasePageLocators.ABOUT), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_number_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "Number phone is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_payment(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_lang_ua(self):
        assert self.click_element(*locators.BasePageLocators.LANGUEGE_BTN), \
            "The element currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.UKRAINIAN_LANG), \
            "The element currency_uah is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_lang_ru(self):
        assert self.click_element(*locators.BasePageLocators.LANGUEGE_BTN), \
            "The element currency is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.RUSSIAN_LANG), \
            "The element currency_usd is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    #def is_element_currency_eur(self):
    #    assert self.click_element(*locators.BasePageLocators.CURRENCY), \
    #        "The element currency is not present or intractable"
    #   assert self.is_element_present(*locators.BasePageLocators.EUR), \
    #        "The element currency_eur is not present"
    #    print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_element_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_DESK), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "The search input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BTN), \
            "The search button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_comparison_button(self):
        assert self.is_element_present(*locators.BasePageLocators.COMPARISON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_inst_button(self):
        assert self.is_element_present(*locators.BasePageLocators.INSTA_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_fb_button(self):
        assert self.is_element_present(*locators.BasePageLocators.FB_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hity_block(self):
        assert self.is_element_present(*locators.BasePageLocators.HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_nout_cat(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW_NOUT_CAT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_used_nout_cat(self):
        assert self.hover_action(*locators.BasePageLocators.USED_NOUT_CAT), \
            "The element is not present"
        
    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.SCREEN_SLIDER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_advertising_unit(self):
        assert self.is_element_present(*locators.BasePageLocators.ADVERTISING_UNIT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_spare_parts(self):
        assert self.hover_action(*locators.MainPageLocators.CAT_SPARE_PARTS), \
            "The element is not present"
        assert self.is_element_present(*locators.MainPageLocators.SUB_CAT_SPARE_PARTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_delivery_block(self):
        assert self.is_element_present(*locators.MainPageLocators.DELIVERY_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_about_block(self):
        assert self.is_element_present(*locators.MainPageLocators.ABOUT_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_payment_block(self):
        assert self.is_element_present(*locators.MainPageLocators.PAYMENT_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_blog_block(self):
        assert self.is_element_present(*locators.MainPageLocators.BLOG_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_contacts_block(self):
        assert self.is_element_present(*locators.MainPageLocators.CONTACTS_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_scroll_to_top_button(self):
        assert self.is_element_present(*locators.MainPageLocators.SCROLL_TO_TOP_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


