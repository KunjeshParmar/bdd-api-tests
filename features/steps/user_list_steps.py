from behave import *
from tests.api_client import get_users_by_page
import json



@when('I request the user list for page 2')
def step_impl(context):
    context.response = get_users_by_page(context.base_url, 2, context.headers)


@then('the response should contain 6 users')
def step_impl(context):
    data = context.response.json()
    assert "data" in data, "No 'data' field in response"
    assert len(data["data"]) == 6, f"Expected 6 users but got {len(data['data'])}"


