import os
import pickle
import random
import string
from pathlib import Path

class Login:
    def __init__(self):
        self.file_utenti = Path("Dati/login.pickle")
        self.file_utenti.parent.mkdir(parents=True, exist_ok=True)
        self.utenti = self.carica_dati() #Dizionario per memorizzare ID e password

    def carica_dati(self):
        try:
            #if os.path.isfile(self.file_utenti):   #self.file_dipendenti.is_file():
                print(f"file {self.file_utenti} trovato")  #os.path.isfile(self.file_dipendenti):
                with open(self.file_utenti, "rb") as file:
                   self.utenti = pickle.load(file)
                return self.utenti

        except (FileNotFoundError, EOFError):
             return {}


    def salva_dati(self):
        try:
            with open(self.file_utenti, "wb") as file:
                pickle.dump(self.utenti, file, pickle.HIGHEST_PROTOCOL)

        except (IOError, pickle.PickleError) as e:
            print(f"Errore durante il salvataggio: {e}")

    def genera_id(self):

        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def registra_utente(self, password):
       """Registra un nuovo utente con un ID random e una password."""
       id_utente = self.genera_id()
       self.utenti[id_utente] = password
       print(f"Registrazione completata! Il tuo ID è: {id_utente} e la tua password è: {password}")
       self.salva_dati()
       return id_utente, password  # Restituisce l'ID generato

    def login(self, id_utente, password):
        """Verifica le credenziali e permette l'accesso."""
        if id_utente in self.utenti and self.utenti[id_utente] == password:
            print("Login effettuato con successo!")
            return True
        else:
            print("ID o password errati.")
            return False
