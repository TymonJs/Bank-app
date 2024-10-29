import unittest
from ..Konto import Konto_Firmowe

class TestCreateBusinessAccount(unittest.TestCase):
    nazwa_firmy = "Testowa firma"
    NIP = 1231231231

    def test_create_business_account(self):
        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)

        self.assertEqual(konto.NIP,self.NIP,"NIP nie został zapisany")

    def test_wrong_NIP(self):
        konto = Konto_Firmowe(self.nazwa_firmy,1234)
        self.assertEqual(konto.NIP,"Niepoprawny NIP!", "NIP nie został zapisany poprawnie")


        

