import unittest
from ..Konto_Osobiste import Konto_Osobiste
from parameterized import parameterized

class TestSendTransfers(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    def setUp(self):
        self.konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
        self.konto.saldo=100
    @parameterized.expand([
        (20,80,"Przelew wychodzący nieudany"),
        (150,100,"Błąd w za dużym przelewie wychodzącym")
    ])
    def test_transfer(self,out,expected,mesg):
        self.konto.przelew_wychodzący(out)
        self.assertEqual(self.konto.saldo,expected,mesg)

    # def test_wyslanie_przelewu(self):
        
    #     konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
    #     konto.saldo = 100
    #     konto.przelew_wychodzący(20)

    #     self.assertEqual(konto.saldo,80,"Przelew nieudany")

    # def test_wyslanie_przelewu_za_duzo(self):

    #     konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
    #     konto.saldo = 80
    #     konto.przelew_wychodzący(100)
    #     self.assertEqual(konto.saldo,80,"Przelew nieudany")

    def test_otrzymanie_przelewu(self):
        konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel)
        konto.przelew_przychodzący(50)

        self.assertEqual(konto.saldo,50,"Przelew nieudany")
