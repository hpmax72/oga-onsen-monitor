import requests
import re

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

# 11/2 = 14個のセルの1番目
cell_1102 = cells[0]

if re.search(r"<a\b", cell_1102):
    print("空室あり")
else:
    print("空室なし")
