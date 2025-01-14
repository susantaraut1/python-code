import smtplib
from email.mime.text import MIMEText 

smtp_server = 'smtp.gmail.com'

port = 587 
sender_email = 'techhube027@gmail.com'
receiver_email = 'techhube027@gmail.com'
message = 'Hello, this is an automated ,message. '

msg = MIMEText(message)
msg['subject'] = 'Automated Email'
msg['from'] = sender_email
msg['to'] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    
    password = input("Enter your Gmail password and press enter:")
    server.login(sender_email, password)
    
    server.sendmail(sender_email,[receiver_email], msg.as_string())
    
     