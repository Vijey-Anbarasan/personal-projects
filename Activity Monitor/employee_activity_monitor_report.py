import datetime
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

import psutil

load_dotenv()

activity_log = []


def capture_activity_and_send_email(start_time, end_time):
    print("Called capture_activity_and_send_email().")
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("PASSWORD")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Employee Activity Report - {datetime.date.today()}"

    email_body = f"Hi,\n\nPlease find your activity from {start_time} to {end_time}:\n\n"
    email_body += "\n".join(activity_log)
    message.attach(MIMEText(email_body, "plain"))

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email Sent successfully.")


def capture_employee_activity():
    print("Called capture_employee_activity().")
    current_time = time.localtime()
    print("Capture employee_activity at  ", current_time)

    if current_time.tm_hour >= 9 and (
            current_time.tm_hour < 19 or (current_time.tm_hour == 19 and current_time.tm_min <= 30)):

        processes = psutil.process_iter(['pid', 'name'])
        applications = [proc.info for proc in processes if proc.info['name'] != 'System Idle Process']

        for app in applications:
            activity_log.append(f"Active Application: {app['name']} (PID: {app['pid']})")
        print("Activity Log : ", activity_log)


def monitor_activity():
    print("Called Monitor Activity.")
    start_time = time.strftime("%H:%M", time.localtime())
    while time.localtime().tm_hour < 18 or (time.localtime().tm_hour == 19 and time.localtime().tm_min <= 30):
        capture_employee_activity()
        print("Time. Local Time_before --> ", time.localtime())
        time.sleep(60)
    end_time = time.strftime("%H:%M", time.localtime())
    capture_activity_and_send_email(start_time, end_time)


if __name__ == "__main__":
    print("--- SCRIPT START ---")
    monitor_activity()
    print("--- SCRIPT END ---")

