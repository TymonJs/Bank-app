import unittest
import requests
from time import time

class TestCreateDeleteAccount(unittest.TestCase):
    data = {"name": "Dave", "surname":"Grohl","pesel":"11111111111"}
    timeout = 0.5
    tries = 100

    def test_wysylanie_usuwanie_kont(self):

        for i in range(self.tries):
            rp = requests.post("http://127.0.0.1:5000/api/accounts",json=self.data,timeout=self.timeout)
            self.assertEqual(rp.status_code,201)
            rd = requests.delete(f"http://127.0.0.1:5000/api/accounts/{self.data["pesel"]}",timeout=self.timeout)
            self.assertEqual(rd.status_code,200)
            

    def test_ksiegowanie_przelewow(self):
        rp = requests.post("http://127.0.0.1:5000/api/accounts",json=self.data)
        for i in range(self.tries):
            rt = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data["pesel"]}/transfer",json={"type":"incoming","amount":100},timeout=self.timeout)
            self.assertEqual(rt.status_code,200)
        
        rd = requests.delete(f"http://127.0.0.1:5000/api/accounts/{self.data["pesel"]}")