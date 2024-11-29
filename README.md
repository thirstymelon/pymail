# Python SMTP Email Sender

This project is a simple script written in Python that demonstrates how to send an email using the SMTP protocol. It connects to an SMTP server (e.g., Gmail) to send an email with a subject and message body.

---

## Features
- Send emails using Gmail's SMTP server.
- Secure email sending using TLS encryption.
- Customizable sender, recipient, subject, and message.

---

## Prerequisites
1. **Python Version**: Python 3.6 or higher is recommended.
2. **Dependencies**: The `smtplib` library (comes pre-installed with Python).
3. **Email Account**: If using Gmail, ensure the following:
   - You have an app-specific password if 2FA is enabled.
   - Allow "less secure apps" or use OAuth2 for better security (if applicable).

---

## How to Use

1. **Clone or Download the Project**:
   ```bash
   git clone https://github.com/<your-username>/smtp-email-sender.git
   cd smtp-email-sender
