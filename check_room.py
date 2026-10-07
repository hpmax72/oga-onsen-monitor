import requests
import re
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header


gmail_user = os.environ.get("GMAIL_USER")
gmail_password = os.environ.get("GMAIL_APP_PASSWORD")

if not gmail_user or not gmail_password:
    print("Gmail設定エラー")
    exit()


def check_room(url, room_id, date, room_name, hotel_name):

    for attempt in range(2):

        try:
            response = requests.get(
                url,
                timeout=30,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )
            response.raise_for_status()
            break

        except requests.RequestException as e:

            if attempt == 0:
                print(hotel_name + " 取得失敗 → 再試行します")
                time.sleep(5)
            else:
                print(hotel_name + " 取得エラー")
                print(e)
                return False

    html = response.text

    room_pos = html.find(room_id)

    if room_pos == -1:
        print(hotel_name + " 部屋ID取得エラー")
        return False

    cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)

    if cal_pos == -1:
        print(hotel_name + " カレンダー取得エラー")
        return False

    tbody_pos = html.find("<tbody", cal_pos)
    tbody_end = html.find("</tbody>", tbody_pos)

    if tbody_pos == -1 or tbody_end == -1:
        print(hotel_name + " 日付データ取得エラー")
        return False

    tbody = html[tbody_pos:tbody_end]

    cells = re.findall(r"<td.*?</td>", tbody, re.S)

    if len(cells) < 1:
        print(hotel_name + " 日付セル取得エラー")
        return False

    cell = cells[0]

    if re.search(r"<a\b", cell):
        print(hotel_name + " " + date + " 空室あり")
        return True

    print(hotel_name + " " + date + " 空室なし")
    return False


oga_url = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

oga_available = check_room(
    oga_url,
    "room_35591",
    "2026年11月2日",
    "SPA SUITE こたつリビング海側（禁煙）（4名定員）",
    "男鹿温泉・別邸つばき"
)


furo_url = "https://reserve.489ban.net/client/furofushi/0/plan/availability/room/stay?date=2026-11-01"

furo_available = check_room(
    furo_url,
    "room_26787",
    "2026年11月1日",
    "モダン和室　禁煙海側（一部客室階段移動あり）",
    "黄金崎不老ふ死温泉"
)


if oga_available or furo_available:

    messages = []

    if oga_available:
        messages.append(
            """【男鹿温泉・別邸つばき】

2026年11月2日に空室が見つかりました。

対象：
SPA SUITE こたつリビング海側（禁煙）（4名定員）

予約サイト：
https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02
"""
        )

    if furo_available:
        messages.append(
            """【黄金崎不老ふ死温泉】

2026年11月1日に空室が見つかりました。

対象：
モダン和室　禁煙海側（一部客室階段移動あり）

予約サイト：
https://reserve.489ban.net/client/furofushi/0/plan/availability/room/stay?date=2026-11-01
"""
        )

    subject = "【空室通知】宿泊予約の空室が見つかりました"

    body = "\n\n".join(messages)

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
