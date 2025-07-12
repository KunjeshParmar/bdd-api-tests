from behave import *
from tests.api_client import delete_user

@when('I send a delete request for user with id {user_id:d}')
def steps_impl(context, user_id):
    context.response = delete_user(context.base_url, user_id, context.headers)