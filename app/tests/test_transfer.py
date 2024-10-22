import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    def test_wyslanie_przelewu(self):
        
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 100
        konto.przelew_wychodzący(20)

        self.assertEqual(konto.saldo,80,"Przelew nieudany")

    def test_otrzymanie_przelewu(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.przelew_przychodzący(50)

        self.assertEqual(konto.saldo,50,"Przelew nieudany")


