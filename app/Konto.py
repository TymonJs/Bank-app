class Konto:
    def __init__(self,imie,nazwisko,pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        if (pesel.length != 11):
            pesel = "Niepoprawny pesel!"
