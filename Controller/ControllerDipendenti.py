from Gestione.Gestione_Dipendenti import Gestione_Dipendenti


class ControllerDipendenti:
    def __init__(self):
        self.gestione_dipendenti = Gestione_Dipendenti()

    def aggiungi_dipendenti(self,codice,nome,mansione,telefono,email):
        self.gestione_dipendenti.aggiungi_dipendenti(codice,nome,mansione,telefono,email)

    def modifica_dipendenti(self,codice,nome,nuovo_nome=None,nuova_mansione=None,nuovo_telefono=None,nuova_email=None):
        self.gestione_dipendenti.modifica_dipendenti(codice,nome,nuovo_nome,nuova_mansione,nuovo_telefono,nuova_email)

    def rimuovi_dipendenti(self,codice):
        self.gestione_dipendenti.rimuovi_dipendenti(codice)

    def ricerca_dipendenti(self,nome):
        self.gestione_dipendenti.ricerca_dipendenti(nome)

    def visualizza_dipendenti(self,ordinati=False):
        self.gestione_dipendenti.visualizza_dipendenti(ordinati)