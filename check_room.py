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

cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)

if cal_pos == -1:
    print("CALENDAR: NOT FOUND")
    exit()

# カレンダー内のtbodyを探す
tbody_pos = html.find("<tbody", cal_pos)

if tbody_pos == -1:
    print("TBODY: NOT FOUND")
    exit()

# tbodyの終了位置
tbody_end = html.find("</tbody>", tbody_pos)

if tbody_end == -1:
    print("TBODY END: NOT FOUND")
    exit()

tbody = html[tbody_pos:tbody_end + len("</tbody>")]

print("\n===== ROOM 35591 TBODY =====")
print(tbody)
print("\n===== END =====")
