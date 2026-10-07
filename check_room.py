import requests
import re

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)

TARGET = "SPA SUITE こたつリビング海側"

if TARGET in html:
    print("TARGET ROOM: FOUND")
else:
    print("TARGET ROOM: NOT FOUND")

# 対象部屋の位置を探す
pos = html.find(TARGET)

if pos == -1:
    print("TARGET ROOM HTML: NOT FOUND")
else:
    print("\n===== TARGET ROOM AREA =====")
    print(html[max(0, pos - 1000):pos + 5000])
    print("\n===== END =====")
