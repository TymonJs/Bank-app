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

    





