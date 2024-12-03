import unittest

from ..Konto_Osobiste import Konto_Osobiste
from parameterized import parameterized

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


    @parameterized.expand([
        (pesel,pesel,"Pesel nie został zapisany!"),
        ("61345678900121312","Niepoprawny pesel!","Pesel nie został przypisany poprawnie")
    ])
    def test_pesel(self,input,expected,msg):
        konto = Konto_Osobiste(self.imie,self.nazwisko,input)

        self.assertEqual(konto.pesel,expected,msg)


    @parameterized.expand([
        (kod_rabatowy,50,"Błąd przy dobryn kodzie "),
        ("kod",0,"Błąd przy złym kodzie"),
        
    ])
    def test_dodawanie_kasy_kodem(self,input,expected,mesg):
        
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel,input)
        self.assertEqual(konto.saldo,expected,mesg)



    #tutaj proszę dodawać nowe testy