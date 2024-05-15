from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.target_help_page import TargetHelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.side_menu_sign_in import SideMenuSignIn
from pages.target_terms_conditions_page import TargetTermsConditionsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.target_help_page = TargetHelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.side_menu_sign_in = SideMenuSignIn(driver)
        self.target_terms_conditions_page = TargetTermsConditionsPage(driver)