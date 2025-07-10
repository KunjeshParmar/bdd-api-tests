from behave import *
from tests.api_client import create_user
import json

@given('the API is up and running')
def step_impl(context):
    pass

@when('I create a user with name "{name}" and job "{job}"')
def step_impl(context, name, job):
    context.response = create_user(context.base_url, name, job, context.headers)


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain the name "{expected_name}"')
def step_impl(context, expected_name):
    response_json = context.response.json()
    assert response_json["name"] == expected_name
