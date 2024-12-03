import unittest
from ..Konto import Konto_Firmowe
from unittest.mock import patch

class TestCreateBusinessAccount(unittest.TestCase):
    nazwa_firmy = "Testowa firma"
    NIP = 8461627563

    def test_create_business_account(self):
        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)

        self.assertEqual(konto.NIP,self.NIP,"NIP nie został zapisany")

    def test_wrong_NIP(self):
        konto = Konto_Firmowe(self.nazwa_firmy,1234)
        self.assertEqual(konto.NIP,"Niepoprawny NIP!", "NIP nie został zapisany poprawnie")

    @patch("app.Konto.Konto_Firmowe.sprawdźNIP")
    def test_unexisting_NIP(self,sprawdźNIP):
        sprawdźNIP.return_value = False
        with self.assertRaises(ValueError) as context:
            Konto_Firmowe(self.nazwa_firmy,1231231231)
            
        self.assertIn("Company not registered!",str(context.exception))    

        

