import os
import pickle
import base64
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = 'credentials.json'
CREDENTIALS_PICKLE = 'token.pickle'

def authenticate_gmail():
    creds = None
    if os.path.exists(CREDENTIALS_PICKLE):
        with open(CREDENTIALS_PICKLE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(CREDENTIALS_PICKLE, 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def send_email(service, sender, to, subject, body):
    message = create_message(sender, to, subject, body)
    try:
        message = service.users().messages().send(userId="me", body=message).execute()
        print(f'Message sent successfully to {to}')
    except HttpError as error:
        print(f'An error occurred: {error}')

def create_message(sender, to, subject, body):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(body)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

if __name__ == '__main__':
    sender = "fgfghg@gmail.com"  # Replace with your email
    to = "dhijm2gmail.co    "# Replace with recipient's email
    subject = "Test Subject"
    body = "This is a test email body."

    service = authenticate_gmail()
    if service:
        send_email(service, sender, to, subject, body)
