import smtplib
from email.mime.text import MIMEText

# Set the SMTP server and login credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "your@email.com"
password = "yourpassword"

# Set the email parameters
recipient = "recipient@email.com"
subject = "Test email from Python"
body = "This is a test email sent from Python."

# Create the email message
msg = MIMEText(body)
msg["Subject"] = subject
msg["To"] = recipient
msg["From"] = username

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()
