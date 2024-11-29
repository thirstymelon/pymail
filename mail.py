import smtplib

def send_email():
    host = "smtp.gmail.com"
    port = 587
    from_email = input("Enter your email address: ").strip()
    password = input("Enter your email password (or app-specific password): ").strip()
    to_email = input("Enter recipient's email address: ").strip()
    subject = input("Enter the email subject: ").strip()
    text = input("Enter the email body: ").strip()

    # Construct the email body
    body = "\r\n".join((
        f"From: {from_email}",
        f"To: {to_email}",
        f"Subject: {subject}",
        "",
        text
    ))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(host, port)
        if port == 587:
            server.starttls()  # Start TLS encryption for port 587
        server.login(from_email, password)  # Log in with credentials
        server.sendmail(from_email, [to_email], body)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # Ensure the server connection is closed

if __name__ == "__main__":
    send_email()
