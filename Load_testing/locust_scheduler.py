import schedule
import time
import os
import webbrowser
import smtplib
from email.message import EmailMessage
from datetime import datetime
import subprocess

def start_locust_ui_and_generate_report():
    print("🚀 Starting Locust Web UI and generating HTML report...")

    # Optional: Kill previous Locust processes (if needed)
    # os.system("pkill -f locust")

    # Step 1: Create a folder for the reports
    report_folder = "locust_reports"
    os.makedirs(report_folder, exist_ok=True)

    # Step 2: Generate timestamped HTML filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"{report_folder}/locust_report_{timestamp}.html"

    # Step 3: Start Locust in non-headless mode (Web UI) and save the report
    command = [
        "locust", "-f", "locustfile.py",
        "--host", "http://localhost:8000",
        "--html", report_filename,  # Save the HTML report
        "-u", "10",    # Number of users
        "-r", "2",     # Rate of user spawning
        "--run-time", "1m",  # Duration of the test
    ]

    # Start Locust process in the background
    subprocess.Popen(command)

    # Step 4: Open Locust Web UI in the default browser
    webbrowser.open("http://localhost:8089")  # Web UI opens at this URL

    print(f"🌐 Locust Web UI launched at http://localhost:8089")
    print(f"📊 Locust HTML report will be saved as {report_filename}")

def send_email(report_file):
    sender_email = "rajavelit22@gmail.com"
    receiver_email = "rajalancer85@gmail.com"
    sender_password = "kslh raub kfag ogyj"

    msg = EmailMessage()
    msg['Subject'] = '📊 Locust Load Test Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the Locust HTML report from today’s load test.')

    try:
        with open(report_file, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='text', subtype='html', filename=os.path.basename(report_file))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print(f"📧 Email sent to {receiver_email} with HTML report attached.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def send_email_dummy_report():
    # Optionally send last HTML report if manually generated
    latest_report = get_latest_report("locust_reports")
    if latest_report:
        send_email(latest_report)
    else:
        print("⚠️ No Locust report found to send.")

def get_latest_report(folder):
    try:
        files = [f for f in os.listdir(folder) if f.endswith(".html")]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
        return os.path.join(folder, files[0]) if files else None
    except:
        return None

# 🕒 Schedule tasks
schedule.every().day.at("14:01").do(start_locust_ui_and_generate_report)  
schedule.every().day.at("14:04").do(send_email_dummy_report)  

print("⏱️ Locust UI Scheduler started. Waiting for scheduled time...")

while True:
    schedule.run_pending()
    time.sleep(1)
