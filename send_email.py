# coding=utf-8

import requests
import smtplib
from email.mime.text import MIMEText

USER = "xxx@qq.com"
PASSWD = "xxx"
TO = "xxx@xxx.com"
TITLE = "raspberry_pi_ip_report"

# get ip

API = "http://www.hahayangqi.cn/a/ip_api.php"
r = requests.get(API)

msg = MIMEText(r.text, "plain", "utf-8")
msg["Subject"] = TITLE
msg["From"] = USER
msg["To"] = TO

s = smtplib.SMTP_SSL("smtp.qq.com", 465)
s.set_debuglevel(1)
s.login(USER, PASSWD)
s.sendmail(USER, TO, msg.as_string())
s.quit()
