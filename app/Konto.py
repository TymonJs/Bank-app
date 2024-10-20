class Konto:
    def __init__(self,imie,nazwisko,pesel,kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel

        if (len(pesel) != 11):
            self.pesel = "Niepoprawny pesel!"

        if kod_rabatowy and "_" in kod_rabatowy and int(pesel[:2])>60:

            promo,kod = kod_rabatowy.split("_")

            if promo=="PROM" and len(kod)==3:
                self.saldo+=50