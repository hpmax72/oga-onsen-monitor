import requests
import re

url = "https://reserve.489ban.net/client/furofushi/0/plan/availability/room/stay?date=2026-11-01"

try:
    r = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("STATUS:", r.status_code)
    print("LENGTH:", len(r.text))

    html = r.text

    room_id = "room_26787"

    room_pos = html.find(room_id)
    print("ROOM ID:", room_pos)

    cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)
    print("CALENDAR:", cal_pos)

    tbody_pos = html.find("<tbody", cal_pos)
    tbody_end = html.find("</tbody>", tbody_pos)

    tbody = html[tbody_pos:tbody_end]

    cells = re.findall(r"<td.*?</td>", tbody, re.S)

    print("CELLS:", len(cells))

    cell = cells[0]

    if re.search(r"<a\b", cell):
        print("11/1: 空室あり")
    else:
        print("11/1: 空室なし")

except Exception as e:
    print("ERROR:")
    print(e)
