import requests

resp = requests.get("https://api.ipify.org?format=json")
print(f"{resp.status_code=}")
print(f"{resp.json()=}")
print("------------------------")
print(f"{resp.request.headers=}")
print(f"{resp.headers=}")