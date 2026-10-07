import requests

URL = "https://reserve.489ban.net/client/ogaonsen/0/plan/availability/room/"

response = requests.get(URL, timeout=30)

print("STATUS:", response.status_code)
print("URL:", response.url)
print("PAGE LENGTH:", len(response.text))

if "SPA SUITE こたつリビング海側（禁煙）(４名定員)" in response.text:
    print("TARGET ROOM: FOUND")
else:
    print("TARGET ROOM: NOT FOUND")

print(response.text[:3000])
