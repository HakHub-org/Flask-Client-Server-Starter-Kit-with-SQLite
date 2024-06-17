"""
Error Reporting
"""

import os
import smtplib
from email.mime.text import MIMEText

def send_error_report(subject, body):
    """
    Send an error report via email.

    Args:
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    config = {
        "smtp_server": os.getenv("SMTP_SERVER"),
        "username": os.getenv("SMTP_USERNAME"),
        "password": os.getenv("SMTP_PASSWORD"),
        "from_address": os.getenv("ERROR_FROM_ADDRESS"),
        "to_address": os.getenv("ERROR_TO_ADDRESS")
    }

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["from_address"]
    msg["To"] = config["to_address"]

    with smtplib.SMTP(config["smtp_server"]) as server:
        server.login(config["username"], config["password"])
        server.sendmail(config["from_address"], [config["to_address"]], msg.as_string())

# Example usage
try:
    # Your code here
    pass
except Exception as e:
    send_error_report("Application Error", str(e))
