import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
import os
from twilio.rest import Client

"""

USAGE: 
import alerts
alerts.email('Hello World', 'My First Email', ['brownconner15@gmail.com'])
alerts.text('My First Text') -> add arguement to = <number> to change recipient

"""

def email(subject, msg, recievers=[]):
    email = config.EMAIL_USERNAME
    password = config.EMAIL_PASSWORD
    for recipient in recievers:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = email
        message["To"] = recipient

        # Create the plain-text and HTML version of your message
        text = msg

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart messageS
        # The email client will try to render the last part first
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            server.sendmail(email, recipient, message.as_string())


def text(msg, to='3195413291'):
    account_sid = config.ACCOUNT_SID
    auth_token = config.SECRET_KEY
    client = Client(account_sid, auth_token)

    message = client.messages .create(body=msg, from_='+14432143979', to=to)

