import unittest

from ..Konto import Konto_Osobiste

class TestCreateBankAccount(unittest.TestCase):

    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "61345678900"
    kod_rabatowy="PROM_AGF"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko , "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_dodawanie_peselu(self):
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        self.assertEqual(konto.pesel, self.pesel, "Pesel nie został zapisany!")

    def test_za_długi_pesel(self):
        konto = Konto_Osobiste(self.imie,self.nazwisko,"61345678900121312")
        self.assertEqual(konto.pesel,"Niepoprawny pesel!", "Pesel nie został przypisany poprawnie")

    def test_dodawanie_kasy_kodem(self):
        
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel,self.kod_rabatowy)
        self.assertEqual(konto.saldo,50,"Kod nie został przyznany")



    #tutaj proszę dodawać nowe testy