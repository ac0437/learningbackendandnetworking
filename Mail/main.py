import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from config import settings

creds = None
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

if os.path.exists('token.json'):
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
  with open('token.json', 'w') as token:
    token.write(creds.to_json())

msg = MIMEMultipart()
msg['From'] = settings.sender_email
msg['To'] = settings.recipient_email
msg['Subject'] = 'test email'

body = 'testing email from pything smtplib script'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(settings.smtp_server, settings.smtp_port)
server.starttls()
server.ehlo()

server.login(settings.sender_email, settings.sender_password)
server.sendmail(settings.sender_email, settings.recipient_email, msg.as_string())

print("Email was sent successfully.")
