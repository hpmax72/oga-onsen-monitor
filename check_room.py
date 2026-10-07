import requests
import re

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)

# 対象文字列を含む場所を全部探す
TARGET = "SPA SUITE こたつリビング海側"

positions = [m.start() for m in re.finditer(TARGET, html)]

print("TARGET COUNT:", len(positions))

for i, pos in enumerate(positions, 1):
    print("\n===== TARGET", i, "=====")
    print(html[max(0, pos - 300):pos + 1500])
    print("===== END =====")
