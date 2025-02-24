import random
import string

class Login:
    def __init__(self):
        self.utenti = {} #Dizionario per memorizzare ID e password

    def genera_id(self):

        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def registra_utente(self, password):
        """Registra un nuovo utente con un ID random e una password."""
        id_utente = self.genera_id()
        self.utenti[id_utente] = password
        print(f"Registrazione completata! Il tuo ID è: {id_utente} e la tua password è: {password}")
        return id_utente, password  # Restituisce l'ID generato

    def login(self, id_utente, password):
        """Verifica le credenziali e permette l'accesso."""
        if id_utente in self.utenti and self.utenti[id_utente] == password:
            print("Login effettuato con successo!")
            return True
        else:
            print("ID o password errati.")
            return False
