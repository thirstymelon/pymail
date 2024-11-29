import smtplib

HOST = "smtp.gmail.com"
PORT = 587  # Use 465 for SSL
SUBJECT = "Test email from Python"
TO = "xyz123@gmail.com"
FROM = "abcd1234@gmail.com"
PASSWORD = "abcd efgh ijkl mnop"  # Use an app-specific password if using Gmail
TEXT = "HeH HeH HeH HeH"

BODY = "\r\n".join((
    f"From: {FROM}",
    f"To: {TO}",
    f"Subject: {SUBJECT}",
    "",
    TEXT
))

try:
    # Connect to SMTP server
    server = smtplib.SMTP(HOST, PORT)
    server.starttls()  # Start TLS encryption
    server.login(FROM, PASSWORD)  # Log in with your credentials
    server.sendmail(FROM, [TO], BODY)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Ensure the server connection is closed
