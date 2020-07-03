"""This script reads the text from a text file and 
emails to a given address"""

import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage


userName = 'myEmail@gmail.com'
loginPass = 'P@SSw0rd'

def send_email(subject, textFile,to_address, from_address=userName):
    
    with open(textFile) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
        msg['Subject'] = subject
        msg['From'] = f"Add Subject Here <{from_address}>"
        msg['To'] = to_address            


    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(userName, loginPass)
    server.sendmail(from_address, to_address, msg.as_string())
    server.close()


if __name__ == '__main__':
    send_email('Subject', 'TextFile.txt','Receiver@gmail.com',)
