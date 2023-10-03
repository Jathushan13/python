
import smtplib, ssl, email
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

f = open('D:\\python\passwords\gmail APass.txt','r')

body = "Ballashan Jeyakumar"
sender_email = 'jathushanj123@gmail.com'
receiver_email = 'jathushan13@outlook.com'
password = f.readline()
bcc = ['niveathan1@outlook.com','haritpatel46050@gmail.com']
all_receiver = [receiver_email] + bcc


msg=MIMEMultipart()
msg['From']='Ballashan Jeyakumar'
msg['To']='jathushan13@outlook.com'
msg["Subject"] = 'selfie for my fans'
msg["Bcc"] = ','.join(bcc)


msg.attach(MIMEText(body, "plain"))

filename = "aj.jpg"

with open('aj.jpg', "rb") as f:
            part = MIMEApplication(
                f.read(),
            )
        # After the file is closed
part['Content-Disposition'] = 'attachment; filename="selfie.jpg"'
msg.attach(part)

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, all_receiver , msg.as_string())

print("email sent successfully")
