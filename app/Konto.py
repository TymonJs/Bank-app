from datetime import datetime
from .SMTPClient import SMTPClient
class Konto:
    def __init__(self):
        self.saldo = 0
        self.historia = []
        self.email_text = "placeholder"

    def przelew_wychodzący(self,kwota):
        if (self.saldo >= kwota):
            self.saldo -= kwota
            self.historia.append(kwota*(-1))
            return True
        return False

    def przelew_przychodzący(self,kwota):
        self.saldo+=kwota
        self.historia.append(kwota)

    def send_history_to_email(self, email, client:SMTPClient):
        date = datetime.today().strftime('%Y-%m-%d')
        subject = f"Wyciąg z dnia {date}"
        text = f"{self.email_text} {self.historia}"
        result = client.send(subject,text,email)
        return result
