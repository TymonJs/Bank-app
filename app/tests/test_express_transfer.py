import unittest

from ..Konto_Firmowe import Konto_Firmowe
from ..Konto_Osobiste import Konto_Osobiste

from unittest.mock import patch

class TestExpresTransfer(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    nazwa_firmy="super firma"
    NIP = 8461627563

    def test_express_transfer_personal_account(self):
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 50

        success = konto.przelew_ekspresowy(29)

        self.assertEqual(success,True)
        self.assertEqual(konto.saldo,20,"Przelew nieudany")

    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def test_express_transfer_business_account(self,sprawdźNIP):
        sprawdźNIP.return_value = True
        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)
        konto.saldo = 50

        success = konto.przelew_ekspresowy(25)

        self.assertEqual(konto.saldo,20,"Przelew nieudany")
        self.assertEqual(success,True)

    def test_express_transfer_too_much_personal(self):

        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 100

        success = konto.przelew_ekspresowy(100)

        self.assertEqual(konto.saldo, 100, "Saldo nie zostało zmniejszone")
        self.assertEqual(success,False)

    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def test_express_transfer_too_much_business(self,sprawdźNIP):

        sprawdźNIP.result_value = True

        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)
        konto.saldo = 100

        success = konto.przelew_ekspresowy(100)

        self.assertEqual(konto.saldo, 100, "Saldo nie zostało zmniejszone")
        self.assertEqual(success,False)



    


