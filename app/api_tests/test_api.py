import unittest
import requests
from ..Konto import Konto_Osobiste

class TestApi(unittest.TestCase):
    data = {"name":"james","surname":"hetfield","pesel":"12312312312"}

    def test_create_account(self):
        
        r = requests.post("http://127.0.0.1:5000/api/accounts", json=self.data)

        self.assertEqual(r.status_code,201,"Accounts hasn't been created")

    def test_get_account_by_pesel(self):

        r = requests.get(f"http://127.0.0.1:5000/api/accounts/{self.data["pesel"]}")

        self.assertEqual(r.status_code,200,"Account not found")

    def test_get_unexisting_account_by_pesel(self):

        r = requests.get(f"http://127.0.0.1:5000/api/accounts/56432")

        self.assertEqual(r.status_code,404,"Pesel search failed")
        