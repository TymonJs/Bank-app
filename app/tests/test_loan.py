import unittest
from parameterized import parameterized
from ..Konto_Firmowe import Konto_Firmowe
from ..Konto_Osobiste import Konto_Osobiste
from unittest.mock import patch

class TestPersonalLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65345678900"

    #def tearDown
    def setUp(self):
        self.konto=Konto_Osobiste(self.imie,self.nazwisko,self.pesel)

    @parameterized.expand([
        ("Last 3 transactions aren't positive",[100,200,300],100,100),
        ("Last 5 transactions aren't greater than the loan",[1000,100,200,300,-200,-100],100,100),
        ("Last 3 transactions are positive",[200,-100,300],100,0),
        ("Last 5 transactions are greater than loan",[1000,100,100,100,-100,-200],100,0)
    ])
    def test_personal_loan(self,name,history,loan,expected):
        self.konto.historia = history

        self.konto.zaciągnij_kredyt(loan)
        self.assertEqual(self.konto.saldo,expected, name)

class TestBusinessLoan(unittest.TestCase):

    NIP=8461627563
    nazwa_firmy="Super firma"

    @patch("app.Konto_Firmowe.Konto_Firmowe.sprawdźNIP")
    def setUp(self,sprawdźNIP):
        sprawdźNIP.return_value=True
        self.konto=Konto_Firmowe(self.nazwa_firmy,self.NIP)

    @parameterized.expand([
        ("Account balance isn't at least 2 times the loan",[1775],100,40,140),
        ("Incorrect balance info",[1775],100,70,100),
        ("Account doesn't have a ZUS payment",[1774],100,40,100)

    ])
    def test_business_loan_balance(self,name,history,saldo,loan,expected):
        

        self.konto.saldo=saldo
        self.konto.historia=history

        self.konto.zaciągnij_kredyt(loan)
        self.assertEqual(self.konto.saldo,expected,name)


    # def test_take_loan_A(self):
        

    #     self.konto.historia = [100,200,300]

    #     self.konto.zaciągnij_kredyt(100)

    #     self.assertEqual(self.konto.saldo,100,"Kredyt nieudany")

    # def test_take_loan_B(self):

    #     self.konto.historia = [1000,100,200,300,-200,-100]

    #     self.konto.zaciągnij_kredyt(100)

    #     self.assertEqual(self.konto.saldo,100,"Kredyt nieudany")

    # def test_take_loan_A_failed(self):


    #     self.konto.historia = [200,-100,300]

    #     self.konto.zaciągnij_kredyt(100)

    #     self.assertEqual(self.konto.saldo,0,"Kredyt nieudany")

    # def test_take_loan_B_failed(self):

    #     self.konto.historia = [1000,100,100,100,-100,-200]

    #     self.konto.zaciągnij_kredyt(100)

    #     self.assertEqual(self.konto.saldo,0,"Kredyt nieudany")
