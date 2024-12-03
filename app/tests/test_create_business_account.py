import unittest
from ..Konto_Firmowe import Konto_Firmowe
from unittest.mock import patch
from parameterized import parameterized


class TestCreateBusinessAccount(unittest.TestCase):
    nazwa_firmy = "Testowa firma"
    NIP = 8461627563
    
    @parameterized.expand([
        (NIP,NIP),
        (1234,"Niepoprawny NIP!")
    ])
    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def test_create_business_account(self,NIP,expected,sprawdźNIP):
        sprawdźNIP.return_value = True
        konto = Konto_Firmowe(self.nazwa_firmy,NIP)

        self.assertEqual(konto.NIP,expected,"NIP nie został zapisany")
        self.assertEqual(konto.saldo,0,"Nazwa firmy nie została zapisana")

   
    @patch("app.Konto_Firmowe.requests.get")
    def test_czy_istnieje(self, mock):
        class Mock:
            status_code = 200
        mock.return_value = Mock()
        self.assertEqual(Konto_Firmowe.sprawdźNIP("0123456789"), True)

    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def test_unexisting_NIP(self,sprawdźNIP):
        sprawdźNIP.return_value = False
        with self.assertRaises(ValueError) as context:
            Konto_Firmowe(self.nazwa_firmy,1231231231)
            
        self.assertIn("Company not registered!",str(context.exception))    

        

