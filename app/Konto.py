import requests
from datetime import datetime
from os import getenv

class Konto:
    def __init__(self):
        self.saldo = 0
        self.historia = []

    def przelew_wychodzący(self,kwota):
        if (self.saldo >= kwota):
            self.saldo -= kwota
            self.historia.append(kwota*(-1))

    def przelew_przychodzący(self,kwota):
        self.saldo+=kwota
        self.historia.append(kwota)

    


class Konto_Osobiste(Konto):
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

        if (len(pesel) != 11):
            self.pesel = "Niepoprawny pesel!"

        if kod_rabatowy and "_" in kod_rabatowy and int(pesel[:2])>60:

            promo,kod = kod_rabatowy.split("_")

            if promo=="PROM" and len(kod)==3:
                self.saldo+=50
    
    def przelew_ekspresowy(self,kwota):
        fee = 1
        opłata = kwota+fee
        if (self.saldo >= opłata):
            self.saldo -= opłata
            self.historia.append(kwota*(-1))
            self.historia.append(fee*(-1))

    def zaciągnij_kredyt(self,kwota):
        # if (len(self.historia)>=3 and all([True if elem > 0 else False for elem in histRev[:3] ])) or (len(self.historia)>=5 and sum(histRev[:5])>kwota):
        if last_three_transasctions_are_positive(self.historia) or last_five_transactions_greater_than_loan(self.historia,kwota):
            self.saldo+=kwota


class Konto_Firmowe(Konto):
    def __init__(self,nazwa_firmy,NIP):
        super().__init__()
        self.nazwa_firmy=nazwa_firmy
        self.NIP=NIP

        if (len(str(NIP)) != 10):
            self.NIP="Niepoprawny NIP!"

        elif not self.sprawdźNIP(NIP):
            raise ValueError("Company not registered!")

    def przelew_ekspresowy(self,kwota):
        fee = 5
        opłata = kwota+fee
        if (self.saldo >= opłata):
            self.saldo -= opłata
            self.historia.append(kwota*(-1))
            self.historia.append(fee*(-1))

    def zaciągnij_kredyt(self,kwota):
        ZUS_payment=1775
        if (self.saldo>2*kwota) and (ZUS_payment in self.historia):
            self.saldo+=kwota
    
    def sprawdźNIP(self,NIP):

        today = datetime.today().strftime('%Y-%m-%d')
        url = getenv("BANK_APP_MF_URL","https://wl-api.mf.gov.pl/api/search/nip/")
        r = requests.get(f"{url}{NIP}?date={today}")
        status = r.status_code==200

        print(f"NIP: {NIP} is {status}")
        return status




def last_three_transasctions_are_positive(hist):
    histRev = hist[::-1]
    if (len(hist)>=3 and all([True if elem > 0 else False for elem in histRev[:3] ])):
        return True
    return False

def last_five_transactions_greater_than_loan(hist,kwota):
    histRev = hist[::-1]
    if (len(hist)>=5 and sum(histRev[:5])>kwota):
        return True
    return False
        