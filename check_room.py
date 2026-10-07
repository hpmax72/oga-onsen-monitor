import requests
import re
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"
ROOM_ID = "room_35591"

try:
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
except requests.RequestException:
    print("取得エラー")
    exit()

html = response.text

room_pos = html.find(ROOM_ID)

if room_pos == -1:
    print("取得エラー")
    exit()

cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)

if cal_pos == -1:
    print("取得エラー")
    exit()

tbody_pos = html.find("<tbody", cal_pos)
tbody_end = html.find("</tbody>", tbody_pos)

if tbody_pos == -1 or tbody_end == -1:
    print("取得エラー")
    exit()

tbody = html[tbody_pos:tbody_end]

cells = re.findall(r"<td.*?</td>", tbody, re.S)

if len(cells) < 1:
    print("取得エラー")
    exit()

cell_1102 = cells[0]

if re.search(r"<a\b", cell_1102):
    print("空室あり")

    gmail_user = os.environ.get("GMAIL_USER")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_password:
        print("Gmail設定エラー")
        exit()

    subject = "男鹿温泉 11/2 空室あり"

    body = """男鹿温泉　結いの宿　別邸つばき

2026年11月2日に空室が見つかりました。

対象：
SPA SUITE こたつリビング海側（禁煙）（4名定員）

予約サイト：
https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02
"""

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = gmail_user
    msg["To"] = gmail_user

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.send_message(msg)

        print("メール送信完了")

    except Exception as e:
        print("メール送信エラー")
        print(e)

else:
    print("空室なし")
