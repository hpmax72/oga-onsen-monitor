import requests
import re

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)

TARGET = "SPA SUITE こたつリビング海側"

print("TARGET ROOM:", "FOUND" if TARGET in html else "NOT FOUND")

# 対象部屋の位置
room_pos = html.find(TARGET)

if room_pos == -1:
    exit()

# room_41319 の位置
room_id = "room_41319"
cal_pos = html.find(room_id, room_pos)

print("ROOM ID:", "FOUND" if cal_pos != -1 else "NOT FOUND")

if cal_pos == -1:
    exit()

print("\n===== CALENDAR AREA =====")
print(html[max(0, cal_pos - 500):cal_pos + 12000])
print("\n===== END =====")
