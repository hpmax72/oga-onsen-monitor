import requests
import re

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)
print("TARGET ROOM: FOUND" if "SPA SUITE こたつリビング海側" in html else "TARGET ROOM: NOT FOUND")

# 11月2日付近のHTMLを探す
for keyword in ["11月2日", "11/2", "2026-11-02", "02"]:
    positions = [m.start() for m in re.finditer(keyword, html)]
    print("KEYWORD:", keyword, "COUNT:", len(positions))

    for pos in positions[:3]:
        print("\n---", keyword, "---")
        print(html[max(0, pos - 500):pos + 1000])
