class Konto:
    def __init__(self):
        self.saldo = 0
        self.historia = []

    def przelew_wychodzący(self,kwota):
        if (self.saldo >= kwota):
            self.saldo -= kwota
            self.historia.append(kwota)

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
            self.historia.append(kwota)
            self.historia.append(fee)



class Konto_Firmowe(Konto):
    def __init__(self,nazwa_firmy,NIP):
        super().__init__()
        self.nazwa_firmy=nazwa_firmy
        self.NIP=NIP

        if (len(str(NIP)) != 10):
            self.NIP="Niepoprawny NIP!"

    def przelew_ekspresowy(self,kwota):
        fee = 5
        opłata = kwota+fee
        if (self.saldo >= opłata):
            self.saldo -= opłata
            self.historia.append(kwota)
            self.historia.append(fee)