
from __future__ import unicode_literals, print_function


# HTML Request sending and parsing
import urllib
from xml.etree import ElementTree
import requests

# Import time utilities for handling the time values
import datetime
import dateutil.parser
import time

# Import the config parser
import yaml

import smtplib
from email.mime.text import MIMEText

def send_email(sender, recipients, subject, body, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

if __name__ == "__main__":
    with open("Arxiv-keyword-email-summary/config.yml", "r") as file:
        params = yaml.safe_load(file)

    send_email(params["sender_email"], params["recipient_email"], params["email_subject"], params["email_content"], params["email_password"])