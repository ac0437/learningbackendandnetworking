<!-- @format -->

# learningbackendandnetworking

## Creating

Started with: https://youtu.be/qqRYkcta6IE

Tutorial was kinda old and I was getting an error: error: read econnreset

Ended with: https://youtu.be/1udhpRy_N6A
that avoided the error.

## Testing

I did not have telnet on my windows device and wasn't looking to install that are any netcat command. Also, wasn't looking to write a powershell script as that was beyond the scope of what I wanted to learn. I was still able to test or see that the servers were up by uing the following powershell commands:

TCP server connection check:
Test-NetConnectionUDP 127.0.0.1 -p 8081

UDP server connection check:
GET-NetUDPEndpoint -LocalAddress 127.0.0.1 -LocalPort 8082

## Mail

1. Create a Google Cloud Project, set up project to be an application, download the JSON file, put it in the working directory, and rename it to crednetials.json
2. Enable the Gmail API
3. Make an application password following the instructions from this tutorial (https://www.youtube.com/watch?v=sCsMfLf1MTg)
4. Create a .env file or encrypted text file to house your passwords and other variables and import to main script
5. Create a token.json file by running this code:

```python
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
```

6. Once you have that you can go create an SMTP server, make a message, login using your user credentials, and send the email:

```python
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
```

NOTE: `setting.smtp_port` has to be 587 and the `settings.sender_password` is the generated password from step 3

## DDos

Follow:

https://www.neuralnine.com/code-a-ddos-script-in-python/

to create a small DDos application using sockets

## Threading

Small threading application to start 10 threads and print hello world

## Port scanner

Follow:
https://www.neuralnine.com/threaded-port-scanner-in-python/

A port scanner that looks at common ports, uncommon ports, or user inputted ports to see if they are open by creating a socket connection. It uses threads to increase the performance of the scanning.
