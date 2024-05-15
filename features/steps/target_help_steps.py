from behave import given, when, then


@given('Open Help page for Returns')
def open_help_page(context):
    context.app.target_help_page.open_help_returns()


@when('Select Help topic Delivery & Pickup')
def select_topic(context):
    context.app.target_help_page.select_topic()


@then('Verify Returns page opened')
def verify_returns_page(context):
    context.app.target_help_page.verify_returns_header()


@then('Verify Drive Up & Order Pickup page opened')
def verify_drive_up_pickup(context):
    context.app.target_help_page.verify_delivery_header()
