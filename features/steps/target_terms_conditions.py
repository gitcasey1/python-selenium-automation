from behave import given, when, then


@given('Store original window')
def store_original_window(context):
    # context.original_window = context.driver.current_window_handle
    # print('Current::', context.original_window)
    context.original_window = context.app.target_terms_conditions_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_target_terms_conditions(context):
    context.app.target_terms_conditions_page.click_target_terms_conditions()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.target_terms_conditions_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_opened(context):
    context.app.target_terms_conditions_page.verify_terms_and_conditions_opened()


@then('User can close new window')
def close_new_window(context):
    context.app.target_terms_conditions_page.close()


@then('Switch back to original window')
def switch_to_original_window(context):
    context.app.target_terms_conditions_page.switch_window_by_id(context.original_window)