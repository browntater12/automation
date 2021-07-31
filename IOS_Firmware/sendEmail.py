import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def email(msg):
    for people in range(len(config.receivers)):
        sender_email = config.emailUsername
        receiver_email = config.receivers[people]
        password = config.emailPassword

        message = MIMEMultipart("alternative")
        message["Subject"] = msg + " IOS VERSION OUT"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = "Apple has released a new version, {} is now available, begin the firmware process.".format(msg)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)

        # Create secure connection with server and send email
        #python2 doesn't support with
        #google servers dont like linx distros playing
        #context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.gmail.com") #, 465, context=context)
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )
        server.quit()
