import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from settings import sets



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

      #def test_login_logout(self, browser):
      #  link_to_site = browser.current_url

    def test_main_page_header(self,browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_blog()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_blog()
        page.is_button_delivery()
        page.is_button_about()
        page.is_number_phone()
        page.is_element_payment()
        page.is_element_lang_ua()
        page.is_element_lang_ru()
        page.is_element_logo()
        page.is_search_input_field()
        page.is_search_button()
        page.is_comparison_button()
        page.is_cart_button()
        page.is_hity_block()
        page.is_inst_button()
        page.is_fb_button()
        page.is_new_nout_cat()
        page.is_used_nout_cat()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider()
        page.is_advertising_unit()
        page.is_cat_spare_parts()
        page.is_about_block()
        page.is_info_block_delivery()
        page.is_payment_block()
        page.is_contacts_block()


    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_scroll_to_top_button()
        




