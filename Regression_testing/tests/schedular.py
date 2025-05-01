import schedule
import time
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

def run_pytest_and_send_html_report():
    print("Running Pytest and generating HTML report...")

    # Step 1: Create a folder to store the report (if not exists)
    report_folder = "pytest_reports"
    os.makedirs(report_folder, exist_ok=True)

    # Generate the filename for the report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"{report_folder}/pytest_report_{timestamp}.html"
    
    # Step 2: Generate HTML report using pytest-html
    os.system(f"pytest --html={report_filename} --self-contained-html")

    # Step 3: Send the HTML report via email
    send_email(report_filename)

def send_email(report_file):
    sender_email = "rajavelit22@gmail.com"
    receiver_email = "rajalancer85@gmail.com"
    sender_password = "kslh raub kfag ogyj" 

    msg = EmailMessage()
    msg['Subject'] = '🧪 Pytest HTML Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the Pytest HTML report from today’s test run.')

    try:
        with open(report_file, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='text', subtype='html', filename=report_file)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print(f"📧 Email sent to {receiver_email} with HTML report attached.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Schedule the task
schedule.every().day.at("13:55").do(run_pytest_and_send_html_report)

print("Scheduler started. Waiting for scheduled time...")

while True:
    schedule.run_pending()
    time.sleep(1)
