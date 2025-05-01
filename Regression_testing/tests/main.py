import streamlit as st
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime
import subprocess
import schedule
import time
import threading

# === Globals ===
report_folder = "pytest_reports"
os.makedirs(report_folder, exist_ok=True)

# === Helper functions ===

def run_pytest_and_generate_report():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"{report_folder}/pytest_report_{timestamp}.html"

    result = subprocess.run(
        ["pytest", f"--html={report_filename}", "--self-contained-html"],
        capture_output=True,
        text=True
    )
    return report_filename, result.stdout, result.stderr

def send_email(report_file, receiver_email):
    sender_email = "rajavelit22@gmail.com"
    sender_password = "kslh raub kfag ogyj"

    msg = EmailMessage()
    msg['Subject'] = '🧪 Pytest HTML Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the Pytest HTML report from today’s test run.')

    try:
        with open(report_file, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='text', subtype='html', filename=os.path.basename(report_file))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return True, "📧 Email sent successfully!"
    except Exception as e:
        return False, f"❌ Failed to send email: {e}"

def run_tests_and_email(receiver_email):
    report_path, stdout, stderr = run_pytest_and_generate_report()
    success, message = send_email(report_path, receiver_email)
    return stdout, stderr, success, message

def start_schedule_job(receiver_email, time_str):
    schedule.clear()
    schedule.every().day.at(time_str).do(run_tests_and_email, receiver_email=receiver_email)
    threading.Thread(target=schedule_runner, daemon=True).start()

def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)

# === Streamlit UI ===

st.title("🧪 Automated Pytest Runner & Email Scheduler")

# Input fields
receiver_email = st.text_input("📥 Enter Receiver Email", value="rajalancer85@gmail.com")
scheduled_time = st.text_input("⏰ Set Daily Run Time (HH:MM, 24hr format)", value="13:55")

# Run now
if st.button("▶ Run Tests & Send Email Now"):
    if receiver_email:
        with st.spinner("Running tests and sending report..."):
            out, err, ok, msg = run_tests_and_email(receiver_email)
            st.text_area("🧾 Pytest Output", out, height=200)
            if err:
                st.error(err)
            if ok:
                st.success(msg)
            else:
                st.error(msg)
    else:
        st.warning("Please enter a valid receiver email.")

# Schedule job
if st.button("📅 Schedule Daily Run"):
    try:
        datetime.strptime(scheduled_time, "%H:%M")  # validate time format
        start_schedule_job(receiver_email, scheduled_time)
        st.success(f"✅ Test run scheduled daily at {scheduled_time} for {receiver_email}")
    except ValueError:
        st.error("Invalid time format! Use HH:MM in 24-hour format.")

# Show latest report
if st.button("📄 Show Latest Report"):
    report_files = sorted(os.listdir(report_folder), reverse=True)
    if report_files:
        latest_report = os.path.join(report_folder, report_files[0])
        with open(latest_report, 'r', encoding='utf-8') as f:
            html = f.read()
        st.components.v1.html(html, height=600, scrolling=True)
    else:
        st.warning("No reports found.")