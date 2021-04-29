#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = input(str("Please key in your email: "))
password = input(str("Please key in your password: "))
email_send = input(str("Please key in your sender mail: "))
subject = input(str("Please key in your subject: "))

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'lai zooba'
msg.attach(MIMEText(body,'plain'))

filename = 'handsome_man.JPG'
attachment =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, password)
print("login successful")

server.sendmail(email_user,email_send,text)
print("Successfully sent email to", email_send)
server.quit()


