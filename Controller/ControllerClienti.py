from Gestione.Gestione_Clienti import Gestione_Clienti


class ControllerClienti:
    def __init__(self):
        self.gestione_clienti = Gestione_Clienti()

    def aggiungi_cliente(self,codice,nome,indirizzo,telefono,email):
        self.gestione_clienti.aggiungi_cliente(codice,nome,indirizzo,telefono,email)

    def modifica_cliente(self,codice,nome,nuovo_nome=None,nuovo_indirizzo=None,nuovo_telefono=None,nuovo_email=None):
        self.gestione_clienti.modifica_cliente(codice,nome,nuovo_nome,nuovo_indirizzo,nuovo_telefono,nuovo_email)

    def rimuovi_cliente(self,codice):
        self.gestione_clienti.rimuovi_cliente(codice)

    def ricerca_cliente(self,nome):
        self.gestione_clienti.ricerca_cliente(nome)

    def visualizza_clienti(self,ordinati=False):
        self.gestione_clienti.visualizza_clienti(ordinati)

    def rimuovi_cliente(self,codice):
        self.gestione_clienti.rimuovi_cliente(codice)

    def ricerca_cliente(self,nome):
        self.gestione_clienti.ricerca_cliente(nome)
