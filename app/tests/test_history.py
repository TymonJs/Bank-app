import unittest

from ..Konto import Konto_Osobiste,Konto_Firmowe

class TestSendTransfers(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    nazwa_firmy = "Testowa firma"
    NIP = 1231231231

    def test_historia_przelewu_konto_osobiste(self):
            konto = Konto_Osobiste(self.imie,self.nazwisko, self.pesel)
            konto.przelew_przychodzący(100)
            konto.przelew_przychodzący(50)
            konto.przelew_wychodzący(10)
            konto.przelew_ekspresowy(100)
            self.assertEqual(konto.historia,[100,50,10,100,1],"Historia została zapisana niepoprawnie")

    def test_historia_przelewu_konto_firmowe(self):
            konto = Konto_Firmowe(self.nazwa_firmy, self.NIP)
            konto.przelew_przychodzący(100)
            konto.przelew_przychodzący(50)
            konto.przelew_wychodzący(10)
            konto.przelew_ekspresowy(100)
            self.assertEqual(konto.historia,[100,50,10,100,5],"Historia została zapisana niepoprawnie")