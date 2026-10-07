import requests

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)

ROOM_ID = "room_35591"

room_pos = html.find(ROOM_ID)

if room_pos == -1:
    print("ROOM 35591: NOT FOUND")
    exit()

print("ROOM 35591: FOUND")

# 対象部屋のカレンダー付近
cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)

if cal_pos == -1:
    print("CALENDAR: NOT FOUND")
    exit()

# 11/2を探す
date_pos = html.find('<span>11/2</span>', cal_pos)

if date_pos == -1:
    print("11/2: NOT FOUND")
    exit()

print("\n===== ROOM 35591 / 11-2 AREA =====")
print(html[date_pos:date_pos + 5000])
print("\n===== END =====")
