# import requests

# r = requests.post("http://127.0.0.1:5000/api/accounts", json={"name":"james","surname":"hetfield","pesel":"12312312312"})

# print(r.status_code)

# curl -X PATCH -H "Content-type: application/json" -d '{"surname":"adam"}' http://127.0.0.1:5000/api/accounts/12312312312

data = {"imie":"james","nazwisko":"hetfield","pesel":"12312312312"}

data2 = {**data, "abc":"asd"}

print(data2)
