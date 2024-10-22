import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    
    def test_wyslanie_przelewu(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "65345678900"
        kod_rabatowy="PROM_ASD"
        konto = Konto(imie,nazwisko,pesel,kod_rabatowy)

        konto.wyslij_przelew(20)

        self.assertEqual(konto.saldo,30,"Przelew nieudany")


