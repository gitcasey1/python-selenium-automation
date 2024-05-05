from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open https://www.target.com/circle')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are 10 benefit cells')
def verify_cells(context):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "div.styles__CellItemContainer-sc-3f68hg-5")
    print(benefit_cells)
    assert len(benefit_cells) == 10, f'Expected 10 benefit cells, got {len(benefit_cells)}'


@when('Click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'addToCartButtonOrTextIdFor13345476').click()


@when('From right side navigation menu, click add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, "[data-test='orderPickupButton']").click()
    sleep(5)


@when('From right side navigation menu, click View cart & check out')
def click_view_cart(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']")


@then('Verify added product is in the cart')
def verify_added_product(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-linked-title']").text
    assert 'Minute Maid Fruit Punch Juice - 59 fl oz' in actual_text, f'Error! Minute Maid Fruit Punch Juice - 59 fl oz not in {actual_text}'
