from datetime import datetime
import requests
from os import getenv 
# # r = requests.post("http://127.0.0.1:5000/api/accounts", json={"name":"james","surname":"hetfield","pesel":"12312312312"})

# # print(r.status_code)

# # curl -X PATCH -H "Content-type: application/json" -d '{"surname":"adam"}' http://127.0.0.1:5000/api/accounts/12312312312

# data = {"imie":"james","nazwisko":"hetfield","pesel":"12312312312"}

# data2 = {**data, "abc":"asd"}

# print(data2)


# r = requests.get("https://wl-api.mf.gov.pl/api/search/nip/8461627563?date=2024-12-01")

# print(r.json()["result"])

print(getenv("BANK_APP_MF_URL","asd"))