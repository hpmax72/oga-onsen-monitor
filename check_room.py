import requests
import re
from datetime import date, timedelta

ROOM_ID = "room_35591"

start_dates = [
    "2026-10-01",
    "2026-10-15",
    "2026-10-29",
    "2026-11-12",
    "2026-11-26",
    "2026-12-10",
]

for start_date in start_dates:

    URL = f"https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date={start_date}"

    response = requests.get(URL, timeout=30)
    html = response.text

    room_pos = html.find(ROOM_ID)

    if room_pos == -1:
        print(start_date, "ROOM NOT FOUND")
        continue

    cal_pos = html.find('<div class="webc_avlbl_cal">', room_pos)

    if cal_pos == -1:
        print(start_date, "CALENDAR NOT FOUND")
        continue

    tbody_pos = html.find("<tbody", cal_pos)
    tbody_end = html.find("</tbody>", tbody_pos)

    tbody = html[tbody_pos:tbody_end]

    print("\n==============================")
    print("START:", start_date)

    # <td>ごとに分割
    cells = re.findall(r"<td.*?</td>", tbody, re.S)

    for i, cell in enumerate(cells, 1):

        if "<a " in cell or "<a>" in cell:

            print("★ LINK FOUND  CELL:", i)
            print(cell.strip())

print("\n===== SEARCH END =====")
