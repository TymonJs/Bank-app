import json
from .Konto_Osobiste import Konto_Osobiste

class AccountRegistry:
    registry= []

    @classmethod
    def add_account(cls,account):
        cls.registry.append(account)

    @classmethod
    def get_accounts_count(cls):
        return len(cls.registry)

    @classmethod
    def search_by_id(cls,id):
        for acc in cls.registry:
            if acc.pesel==id:
                return acc
        return None
    @classmethod
    def delete_account(cls,pesel):
        cls.registry.remove(cls.search_by_id(pesel))

    @classmethod
    def load_registry(cls):
        cls.registry = []
        try:
            with open("registry_backup.json","r") as backup:
                data = json.load(backup)
                if data["registry"]:
                    updated = []
                    for person in data["registry"]:
                        k = Konto_Osobiste(
                            person["imie"],
                            person["nazwisko"],
                            person["pesel"]
                        )
                        k.saldo = person["saldo"],
                        k.historia = person["historia"]
                        
                        updated.append(k)
                    cls.registry=updated
                return True
        except FileNotFoundError:
            return False
        
    @classmethod
    def save_registry(cls):
        with open("registry_backup.json","w",encoding="utf-8") as backup:
            keys = ["imie","nazwisko","pesel","saldo","historia"]
            data = [
                {key:getattr(konto,key) for key in keys}
                for konto in cls.registry
            ]
            json.dump({"registry":data},backup,indent=4)



    

    