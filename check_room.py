import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

gmail_user = os.environ.get("GMAIL_USER")
gmail_password = os.environ.get("GMAIL_APP_PASSWORD")

if not gmail_user or not gmail_password:
    print("Gmail設定エラー")
    exit()

to_address = gmail_user

subject = "【テスト】男鹿温泉 空室監視"

body = """これは空室監視メールの送信テストです。

GitHub ActionsからGmailの送信テストを行っています。
"""

msg = MIMEText(body, "plain", "utf-8")
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = gmail_user
msg["To"] = to_address

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.send_message(msg)

    print("メール送信完了")

except Exception as e:
    print("メール送信エラー")
    print(e)
