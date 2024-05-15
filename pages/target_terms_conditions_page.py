from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetTermsConditionsPage(Page):
    TARGET_TERMS_CONDITIONS = (By.XPATH, "//a[text()='Target terms and conditions']")

    def click_target_terms_conditions(self):
        self.click(*self.TARGET_TERMS_CONDITIONS)

    def verify_terms_and_conditions_opened(self):
        self.verify_partial_url('terms-conditions')

