
import requests

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

except Exception as e:
    print("ERROR:")
    print(e)
