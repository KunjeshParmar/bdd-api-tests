# features/steps/common_steps.py
from behave import given, then

@given('the Reqres API is available')
def step_impl(context):
    pass

@then('the response status should be {expected_status:d}')
def step_impl(context, expected_status):
    assert context.response.status_code == expected_status, \
        f"Expected {expected_status}, got {context.response.status_code}"
