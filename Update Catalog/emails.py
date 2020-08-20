from email.message import EmailMessage
import mimetypes
import smtplib
import os

def generate_message(sender, recipient, subject, body, attachment_path):
        message = EmailMessage()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.set_content(body)

        if attachment_path !=  "":
                attachment_filename = os.path.basename(attachment_path)
                full_mime_type, _ = mimetypes.guess_type(attachment_path)
                mime_type, mime_subtype = full_mime_type.split('/', 1)

                with open(attachment_path, 'rb') as attachment:
                        message.add_attachment(attachment.read(), maintype = mime_type, subtype = mime_subtype, filename = attachment_filename)
        return message

def send_message(message):
        mail_server = smtplib.SMTP('localhost')
        mail_server.send_message(message)
        mail_server.quit()
