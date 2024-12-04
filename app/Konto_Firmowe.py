from .Konto import Konto
import requests
from datetime import datetime
from os import getenv


class Konto_Firmowe(Konto):
    def __init__(self,nazwa_firmy,NIP):
        super().__init__()
        self.nazwa_firmy=nazwa_firmy
        self.NIP=NIP

        if (len(str(NIP)) != 10):
            self.NIP="Niepoprawny NIP!"

        elif not Konto_Firmowe.sprawdźNIP(NIP):
            raise ValueError("Company not registered!")

    def przelew_ekspresowy(self,kwota):
        fee = 5
        opłata = kwota+fee
        if (self.saldo >= opłata):
            self.saldo -= opłata
            self.historia.append(kwota*(-1))
            self.historia.append(fee*(-1))
            return True
        return False

    def zaciągnij_kredyt(self,kwota):
        ZUS_payment=1775
        if (self.saldo>2*kwota) and (ZUS_payment in self.historia):
            self.saldo+=kwota
    
    @staticmethod
    def sprawdźNIP(NIP):
        today = datetime.today().strftime('%Y-%m-%d')
        url = getenv("BANK_APP_MF_URL","https://wl-api.mf.gov.pl/api/search/nip/")
        r = requests.get(f"{url}{NIP}?date={today}")
        status = r.status_code==200

        print(f"NIP: {NIP} is {status}")
        return status




