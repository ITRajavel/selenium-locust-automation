import streamlit as st
import os
import smtplib
import subprocess
import threading
import time
import webbrowser
from datetime import datetime
from email.message import EmailMessage

# === Helper functions ===

def generate_locust_command(users, rate, run_time, report_filename):
    return [
        "locust", "-f", "locustfile.py",
        "--host", "https://fakestoreapi.com",
        "--headless",
        "--html", report_filename,
        "-u", str(users),
        "-r", str(rate),
        "--run-time", run_time
    ]

def start_locust_test(users, rate, run_time):
    folder = "locust_reports"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"{folder}/locust_report_{timestamp}.html"

    command = generate_locust_command(users, rate, run_time, report_file)

    # Start Locust in background and open UI
    subprocess.Popen(["locust", "-f", "locustfile.py", "--host", "https://fakestoreapi.com"])
    webbrowser.open("http://localhost:8089")

    # Start headless test in another thread
    threading.Thread(target=lambda: subprocess.run(command)).start()

    return report_file

def send_email(report_file, receiver_email):
    sender_email = "rajavelit22@gmail.com"
    sender_password = "kslh raub kfag ogyj"  # Use Gmail App Password

    msg = EmailMessage()
    msg['Subject'] = '📊 Locust Load Test Report'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Attached is the Locust HTML report from today’s load test.')

    try:
        with open(report_file, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='html', filename=os.path.basename(report_file))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.set_debuglevel(1)  # Debug SMTP
            smtp.login(sender_email, sender_password)
            time.sleep(3)
            smtp.send_message(msg)

        return True, "📧 Email sent successfully!"
    except Exception as e:
        return False, f"❌ Failed to send email: {e}"

def convert_time_to_seconds(run_time):
    try:
        if run_time.endswith('m'):
            return int(run_time[:-1]) * 60
        elif run_time.endswith('s'):
            return int(run_time[:-1])
        else:
            return int(run_time)
    except:
        return 60

# === Streamlit UI ===

st.title("🐞 Locust Test → Email Report")

receiver_email = st.text_input("📥 Receiver Email", value="rajalancer85@gmail.com")
users = st.number_input("👤 Number of Users", min_value=1, value=10)
spawn_rate = st.number_input("⚡ Spawn Rate", min_value=1, value=2)
run_time = st.text_input("⏱️ Run Time (e.g., 1m, 30s)", value="1m")

if st.button("🚀 Run Locust Test & Email Report"):
    if not receiver_email:
        st.warning("Please enter a receiver email.")
    else:
        with st.spinner("Starting Locust UI and test..."):
            report_file = start_locust_test(users, spawn_rate, run_time)
            wait_time = convert_time_to_seconds(run_time) + 5  # Add buffer
            time.sleep(wait_time)

            if os.path.exists(report_file):
                success, message = send_email(report_file, receiver_email)
                if success:
                    st.success(f"✅ Report emailed successfully!\n\n📄 Report: `{report_file}`")
                else:
                    st.error(message)
            else:
                st.error("❌ Report was not generated within expected time.")
