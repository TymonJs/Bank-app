import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "12345678900"
        pierwsze_konto = Konto(imie,nazwisko,pesel)

        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko , "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_dodawanie_peselu(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "12345678900"
        konto = Konto(imie,nazwisko,pesel)

        self.assertEqual(konto.pesel, pesel, "Pesel nie został zapisany!")

    def test_dodawanie_kasy_kodem(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "61345678900"
        kod_rabatowy="PROM_AGF"
        konto = Konto(imie,nazwisko,pesel,kod_rabatowy)
        self.assertEqual(konto.saldo,50,"Kod nie został przyznany")



    #tutaj proszę dodawać nowe testy