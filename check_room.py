import requests
import re

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/stay?date=2026-11-02"

response = requests.get(URL, timeout=30)
html = response.text

print("STATUS:", response.status_code)

TARGET = "SPA SUITE こたつリビング海側"

positions = [m.start() for m in re.finditer(TARGET, html)]

print("TARGET COUNT:", len(positions))

for i, pos in enumerate(positions, 1):

    # 次の対象部屋までの範囲だけを見る
    next_pos = positions[i] if i < len(positions) else pos + 5000
    area = html[pos:next_pos]

    # room_XXXXX を探す
    room_ids = re.findall(r'room_(\d+)', area)

    # 定員を探す
    capacity = re.search(r'（([０-９0-9]+)名定員）', area)

    print("\n===== TARGET", i, "=====")

    if capacity:
        print("CAPACITY:", capacity.group(1), "名")
    else:
        print("CAPACITY: NOT FOUND")

    if room_ids:
        print("ROOM ID:", room_ids[0])
    else:
        print("ROOM ID: NOT FOUND")

    print("ROOM IDS FOUND:", room_ids)

    print("===== END =====")
