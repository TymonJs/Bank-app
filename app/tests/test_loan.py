import unittest

from ..Konto import Konto_Osobiste,Konto_Firmowe

class TestLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    def test_take_loan_A(self):
        konto=Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        konto.przelew_przychodzący(100)
        konto.przelew_przychodzący(200)
        konto.przelew_przychodzący(300)

        konto.zaciągnij_kredyt(100)

        self.assertEqual(konto.saldo,700,"Kredyt nieudany")

    def test_take_loan_B(self):
        konto=Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        konto.przelew_przychodzący(1000)
        konto.przelew_przychodzący(100)
        konto.przelew_przychodzący(200)
        konto.przelew_przychodzący(300)

        konto.przelew_wychodzący(200)
        konto.przelew_wychodzący(100)

        konto.zaciągnij_kredyt(100)

        self.assertEqual(konto.saldo,1400,"Kredyt nieudany")

    def test_take_loan_A_failed(self):
        konto=Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        konto.przelew_przychodzący(200)
        konto.przelew_wychodzący(100)
        konto.przelew_przychodzący(300)
        konto.zaciągnij_kredyt(100)

        self.assertEqual(konto.saldo,400,"Kredyt nieudany")

    def test_take_loan_B_failed(self):
        konto=Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

        konto.przelew_przychodzący(1000)
        konto.przelew_przychodzący(100)
        konto.przelew_przychodzący(100)
        konto.przelew_przychodzący(100)

        konto.przelew_wychodzący(100)
        konto.przelew_wychodzący(200)

        konto.zaciągnij_kredyt(100)

        self.assertEqual(konto.saldo,1000,"Kredyt nieudany")
