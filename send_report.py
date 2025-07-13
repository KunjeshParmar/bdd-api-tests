from tests.email_utils import send_allure_report

# Replace with your real credentials or load from env variables
EMAIL = "kmsparmar.1993@gmail.com"
APP_PASSWORD = "ytkj mylq kvvw ntsv"
TO_EMAIL = "kmspguru@gmail.com"

send_allure_report(EMAIL, APP_PASSWORD, TO_EMAIL)
