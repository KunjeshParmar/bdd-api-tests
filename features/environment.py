def before_all(context):
    context.base_url = "https://reqres.in/api"
    context.headers = {"x-api-key": "reqres-free-v1"}

