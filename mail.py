# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formatdate
import os
import codecs


mail_host = 'smtp.163.com'
mail_user = 'qinfen_python@163.com'
mail_pass = '562059487'
sender = 'qinfen_python@163.com'


class Mail163:

    def __init__(self,receiver,subject=mail_user):
        self.receiver = receiver
        self.message = MIMEMultipart()
        self.message['From'] = sender
        self.message['To'] = self.receiver
        self.message['Subject'] = subject
        self.message['Date'] = formatdate()

    def sendmsg(self,content):
        self.mtext = MIMEText(content,'plain','utf-8')
        self.message.attach(self.mtext)
        self.send()

    def sendfile(self,filename):

        basename = os.path.basename(filename)
        with open(filename) as f:
            content = f.read()
            self.mtext = MIMEText(content,'plain','utf-8')

            # 附件设置内容类型，方便起见，设置为二进制流
            self.mtext['Content-Type'] = 'application/octet-stream'
            # 设置附件头，添加文件名
            self.mtext['Content-Disposition'] = 'attachment;filename=%s'%basename
            # 解决中文附件名乱码问题
            # self.mtext.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))

            self.message.attach(self.mtext)

            self.send()

    def send(self):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            # 需要SSL认证
            # smtpObj = smtplib.SMTP_SSL(mail_host)

            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, self.receiver, self.message.as_string())
            print('success')
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print('error', e)


if __name__ == "__main__":
    mai = Mail163("yuechaoqun@zhixunkeji.cn","2018/10/11 树苗销售情况")
    mai.sendmsg(r"C:\Users\Administrator\Desktop\work\test.csv")


