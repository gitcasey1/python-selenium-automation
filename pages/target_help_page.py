from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page


class TargetHelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_DELIVERY = (By.XPATH, "//h1[text()=' Drive Up & Order Pickup']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value('Delivery & Pickup')

    def verify_returns_header(self):
        self.wait_until_visible(*self.HEADER_RETURNS)

    def verify_delivery_header(self):
        self.wait_until_visible(*self.HEADER_DELIVERY)