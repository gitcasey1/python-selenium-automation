from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(5)


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem").text
    assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not in {actual_text}'


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.styles__LinkText-sc-1e1g60c-3.dZfgoT.h-margin-r-x3").click()
    sleep(5)


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
    assert 'Sign into your Target account' in actual_text, f'Error! Text Sign into your Target account not in {actual_text}'


@when('Search for {beverage}')
def search_beverage(context, beverage):
    context.driver.find_element(By.ID, 'search').send_keys(beverage)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()


@then('Verify user sees search results for {beverage}')
def verify_search(context, beverage):
    search_results = context.driver.find_element(By.XPATH, "//span[text()='for “juice”']").text
    assert beverage in search_results, f'Error! Search result for {beverage} not in {search_results}'