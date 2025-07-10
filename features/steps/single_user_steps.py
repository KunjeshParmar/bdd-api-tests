from behave import *
from tests.api_client import get_single_user



@when("I request the details of user with ID 2")
def step_impl(context):
    context.response= get_single_user(context.base_url, 2, context.headers)



@step('the response should contain the first name "Janet"')
def step_impl(context):
    data= context.response.json()
    assert data["data"]["first_name"] == "Janet", f"Expected 'Janet', got '{data['data']['first_name']}'"