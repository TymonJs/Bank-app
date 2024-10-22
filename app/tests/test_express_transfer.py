import unittest

from ..Konto import Konto_Osobiste,Konto_Firmowe

class TestExpresTransfer(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    nazwa_firmy="super firma"
    NIP = 1231231231

    def test_express_transfer_personal_account(self):
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 50

        konto.przelew_ekspresowy(29)

        self.assertEqual(konto.saldo,20,"Przelew nieudany")

    def test_express_transfer_business_account(self):
        konto = Konto_Firmowe(self.nazwa_firmy,self.NIP)
        konto.saldo = 50

        konto.przelew_ekspresowy(25)

        self.assertEqual(konto.saldo,20,"Przelew nieudany")


    


