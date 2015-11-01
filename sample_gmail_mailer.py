import smtplib
import getpass
import email
import email.mime.application
import mimetypes
def main():
    server=smtplib.SMTP('smtp.gmail.com',587)
    username=raw_input("Enter username:")
    password=getpass.getpass()
    receiver=raw_input("Enter reciever name:")
    server.ehlo()
    server.starttls()
    server.login(username,password)
    text=raw_input("Enter msg:")
    body=email.mime.Text.MIMEText(text)
    msg=email.mime.Multipart.MIMEMultipart()
    msg['Subject']="Email"
    msg['From']=username
    msg['To']=receiver
    msg.attach(body)
    attach_flag=raw_input("Add attachments? 1- yes 0 -no")
    while(attach_flag=="1"):
        filename=raw_input("Enter filename: (With path)")
        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read())
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)
        attach_flag=raw_input("Add more attachments? 1- yes 0 -no")
            
    server.sendmail(username,receiver,msg.as_string())
    server.close()
if __name__=='__main__':
    main()
