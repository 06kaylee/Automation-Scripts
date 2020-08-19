from email.message import EmailMessage
import mimetypes
import smtplib
import pathlib
import getpass

def generate_message(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    
    attachment_filename = attachment_path.name
    full_mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = full_mime_type.split('/', 1)

    with open(attachment_path, 'rb') as attachment:
        message.add_attachment(attachment.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)

    return message

def send(message):
    server = smtplib.SMTP_SSL('smtp.example.com')
    server.connect('smtp.example.com', 465)
    password = getpass.getpass()
    server.login("<user>@example.com", password)
    server.send_message(message)
    print("Email has been sent.")
    server.quit()
