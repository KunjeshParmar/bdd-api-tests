from behave import when, then
from tests.api_client import update_user

@when('I update the user with ID {user_id:d} with name "{name}" and job "{job}"')
def step_impl(context, user_id, name, job):
    context.response = update_user(context.base_url, user_id, name, job, context.headers)

@then('the response should contain the job "{expected_job}"')
def step_impl(context, expected_job):
    data = context.response.json()
    assert data["job"] == expected_job, f"Expected job '{expected_job}' but got '{data.get('job')}'"
