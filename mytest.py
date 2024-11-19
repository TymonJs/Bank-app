import requests

r = requests.post("http://127.0.0.1:5000/api/accounts", json={"name":"james","surname":"hetfield","pesel":"12312312312"})

print(r.status_code)