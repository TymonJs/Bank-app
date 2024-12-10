import unittest

from ..Konto_Firmowe import Konto_Firmowe
from ..Konto_Osobiste import Konto_Osobiste
from ..SMTPClient import SMTPClient

from parameterized import parameterized
from unittest.mock import patch,MagicMock

class TestSMTP(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    nazwa_firmy = "Testowa firma"
    NIP = 8461627563
 
    email="darek.janusz@gmail.com"

    
    
    @parameterized.expand([
        (True,True,Konto_Osobiste,"Error during sending personal account history"),
        (False,False,Konto_Osobiste,"Error during false-sending personal account history")
    ])
    def test_send_history_personal(self,return_value,expected,acc,msg):
        client = SMTPClient()
        konto = acc(self.imie,self.nazwisko,self.pesel)
        konto.historia = [100,200,-50]
        client.send = MagicMock(return_value=return_value)
        result = konto.send_history_to_email(self.email,client)
        self.assertEqual(result,expected,msg)
        client.send.assert_called_once()


    @parameterized.expand([
        (True,True,"Error during sending business account history"),
        (False,False,"Error during false-sending business account history")
    ])
    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def test_send_history_business(self,ret_val,expected,msg,sprawdźNIP):
        sprawdźNIP.return_value = True
        client = SMTPClient()
        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)
        konto.historia = [100,200,-50]
        client.send = MagicMock(return_value=ret_val)
        result = konto.send_history_to_email(self.email,client)
        self.assertEqual(result,expected,msg)

    def test_SMTP_send(self):
        smtp_client = SMTPClient()
        smtp_client.send = MagicMock(return_value=True)
        smtp_client.send("Temat","Text","Email")
        smtp_client.send.assert_called_once()
        smtp_client.send.assert_called_with("Temat","Text","Email")
