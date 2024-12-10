from .Konto import Konto
from datetime import datetime
from .SMTPClient import SMTPClient

class Konto_Osobiste(Konto):
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.email_text = "Twoja historia konto to"

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
            return True
        return False

    def zaciągnij_kredyt(self,kwota):
        # if (len(self.historia)>=3 and all([True if elem > 0 else False for elem in histRev[:3] ])) or (len(self.historia)>=5 and sum(histRev[:5])>kwota):
        if last_three_transasctions_are_positive(self.historia) or last_five_transactions_greater_than_loan(self.historia,kwota):
            self.saldo+=kwota


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
        