from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SideMenuSignIn(Page):
    SIDE_MENU_SIGN_IN = (By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']")

    def click_sign_in(self):
        self.click(*self.SIDE_MENU_SIGN_IN)
        sleep(3)
