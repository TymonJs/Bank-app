import unittest

from ..AccountsRegistry import AccountsRegistry
from ..Konto import Konto_Osobiste

class TestAccountsRegistry(unittest.TestCase):

    imie="Dariusz"
    nazwisko="Januszewski"
    pesel1 = "12312312312"
    pesel2 = "23423423423"
    pesel3 = "34534534534"

    def setUp(self):
        AccountsRegistry.registry = []
        self.konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel1)
        AccountsRegistry.add_account(self.konto)

    def test_add_account(self):
        self.assertEqual(AccountsRegistry.registry[0],self.konto,"Account didn't get added")

    def test_accounts_count(self):
        self.assertEqual(AccountsRegistry.get_accounts_count(),1,"Account count doesn't match")

    def test_search_account_by_id(self):
        konto2 = Konto_Osobiste(self.imie,self.nazwisko,self.pesel2)
        konto3 = Konto_Osobiste(self.imie,self.nazwisko,self.pesel3)
        AccountsRegistry.add_account(konto2)
        AccountsRegistry.add_account(konto3)

        self.assertEqual(AccountsRegistry.search_by_id(self.pesel1),self.konto,"Registry didn't search for the correct account")        

