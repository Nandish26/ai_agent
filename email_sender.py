import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,password

# Email details
def send_email(receiver_email,subject,content):

    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Connect to Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

send_email(receiver_email="4mh23cs129a@gmail.com",subject="Test Email from Python",content="Hello! This email was sent using Python 🚀")