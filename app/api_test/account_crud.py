import unittest
import requests
from ..Konto_Osobiste import Konto_Osobiste
class TestApi(unittest.TestCase):
    data = {"name":"james","surname":"hetfield","pesel":"12312312312"}
    fullData = {**data,"balance":0}

    def setUp(self):
        r = requests.post("http://127.0.0.1:5000/api/accounts",json=self.data)
        self.assertEqual(r.status_code,201)

    def tearDown(self):
        r = requests.delete(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}")
        self.assertEqual(r.status_code,200)

    def test_get_account_by_pesel(self):

        r = requests.get(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}")
        self.assertEqual(r.status_code,200,"Account not found")
        self.assertEqual(r.json(),self.fullData,"Wrong account was found")

    def test_get_unexisting_account_by_pesel(self):
        r = requests.get(f"http://127.0.0.1:5000/api/accounts/56432")

        self.assertEqual(r.status_code,404,"Pesel search failed")
        
    def test_update_account(self):
        r = requests.patch(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}",json={"name":"adam"})

        self.assertEqual(r.status_code,200,"Account hasn't been updated")

    def test_pesel_already_taken(self):
        r = requests.post("http://127.0.0.1:5000/api/accounts",json=self.data)

        self.assertEqual(r.status_code,409)

    def test_transfer_incoming(self):
        r = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"incoming","amount":500})
        self.assertEqual(r.status_code,200)
    
    def test_transfer_outgoing(self):
        requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"incoming","amount":1000})

        r = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"outgoing","amount":500})
        self.assertEqual(r.status_code,200)

    def test_transfer_outgoing_express(self):
        requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"incoming","amount":1000})

        r = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"express","amount":500})
        self.assertEqual(r.status_code,200)

    def test_transfer_outgoing_too_much(self):
        requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}",json={"type":"incoming","amount":100})

        r = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"outgoing","amount":500})
        self.assertEqual(r.status_code,422)

    def test_transfer_wrong_type(self):
        r = requests.post(f"http://127.0.0.1:5000/api/accounts/{self.data['pesel']}/transfer",json={"type":"none","amount":500})
        self.assertEqual(r.status_code,405)