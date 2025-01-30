import unittest
import json

from ..AccountRegistry import AccountRegistry
from ..Konto_Osobiste import Konto_Osobiste

class TestAccountsRegistry(unittest.TestCase):

    imie="Dariusz"
    nazwisko="Januszewski"
    pesel1 = "12312312312"
    pesel2 = "23423423423"
    pesel3 = "34534534534"

    def setUp(self):
        AccountRegistry.registry = []
        self.konto = Konto_Osobiste(self.imie,self.nazwisko,self.pesel1)
        AccountRegistry.add_account(self.konto)

    def test_add_account(self):
        self.assertEqual(AccountRegistry.registry[0],self.konto,"Account didn't get added")

    def test_accounts_count(self):
        self.assertEqual(AccountRegistry.get_accounts_count(),1,"Account count doesn't match")

    def test_delete_account(self):
        AccountRegistry.delete_account(self.pesel1)
        self.assertEqual(AccountRegistry.search_by_id(self.pesel1),None,"Account didn't get deleted")
        
    def test_search_account_by_id(self):
        konto2 = Konto_Osobiste(self.imie,self.nazwisko,self.pesel2)
        konto3 = Konto_Osobiste(self.imie,self.nazwisko,self.pesel3)
        AccountRegistry.add_account(konto2)
        AccountRegistry.add_account(konto3)

        self.assertEqual(AccountRegistry.search_by_id(self.pesel1),self.konto,"Registry didn't search for the correct account")        

    def test_save_backup(self):
        AccountRegistry.save_registry()
        try:
            with open("registry_backup.json","r",encoding="utf-8") as backup:
                reg = json.load(backup)
                self.assertEqual(len(reg["registry"]),1)
        except:
            self.assertEqual(True,False)
    
    def test_load_backup(self):
        regBefore = AccountRegistry.registry
        AccountRegistry.load_registry()
        regAfter = AccountRegistry.registry
        self.assertNotEqual(regBefore,regAfter)

        



