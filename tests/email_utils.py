import smtplib
import os
import zipfile
from email.message import EmailMessage

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, folder_path))

def send_allure_report(email_address, password, to_address):
    folder_to_zip = "allure-report"
    zip_file_name = "allure-report.zip"

    zip_folder(folder_to_zip, zip_file_name)

    msg = EmailMessage()
    msg['Subject'] = 'BDD Automation - Allure Test Report'
    msg['From'] = email_address
    msg['To'] = to_address
    msg.set_content('Hi,\n\nPlease find attached the latest Allure test report.\n\nRegards,\nKunjesh')

    with open(zip_file_name, 'rb') as f:
        msg.set_content(
    "Hi,\n\nThe Allure test report has been generated.\n\n"
    "🔗 You can download it from: https://your-report-link.com\n\n"
    "Regards,\nKunjesh"
)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, password)
        smtp.send_message(msg)
